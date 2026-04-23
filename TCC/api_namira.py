from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime
import locale
import os
import PyPDF2
import json

def obter_numero_semana_formatado(semanas_retroceder=0):
    hoje = datetime.date.today()
    # Retroceder semanas, se necessário
    segunda_feira = hoje - datetime.timedelta(days=hoje.weekday(), weeks=semanas_retroceder)

    numero_semana = segunda_feira.isocalendar().week

    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    data_formatada = segunda_feira.strftime("%d de %B de %Y")

    return f"Semana Epidemiológica {(numero_semana - 2 )} - {data_formatada}"

def baixar_boletim_mais_recente():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://capital.sp.gov.br/web/saude/w/vigilancia_em_saude/boletim_covisa/267596")

    tentativas = 3
    semanas_retrocedidas = 0

    # Caminho seguro relativo ao projeto
    pasta_destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Dados", "PDF")
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, "boletim.pdf")

    while semanas_retrocedidas < tentativas:
        semana = obter_numero_semana_formatado(semanas_retrocedidas)
        wait = WebDriverWait(driver, 5)

        try:
            boletins_list = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{semana}']")))
            link_boletim = boletins_list.get_attribute("href")

            if link_boletim:
                driver.get(link_boletim)
                response = requests.get(link_boletim, stream=True)
                with open(caminho_arquivo, "wb") as pdf_file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            pdf_file.write(chunk)
                print("Boletim baixado com sucesso!")
                break
            else:
                raise Exception("Link do boletim não encontrado.")

        except Exception as e:
            print(f"Tentativa {semanas_retrocedidas + 1}: {e}")
            semanas_retrocedidas += 1
            if semanas_retrocedidas >= tentativas:
                print("Não foi possível encontrar o boletim nas semanas verificadas.")
                break

    driver.quit()

    paginas_desejadas = [10, 11]
    return extrair_dados_paginas(caminho_arquivo, paginas_desejadas)

def extrair_dados_paginas(caminho_arquivo, paginas):
  
  try:
    # Abre o arquivo PDF
    with open(caminho_arquivo, "rb") as arquivo_pdf:
      leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

      # Extrai o texto das páginas especificadas
      texto_total = ""
      for pagina_numero in paginas:
        pagina = leitor_pdf.pages[pagina_numero]
        texto_pagina = pagina.extract_text()
        texto_total += texto_pagina

      # Divide o texto em linhas
      linhas = texto_total.splitlines()

      # Extrai os dados de cada linha
      dados_extraidos = []
      for linha in linhas:
        partes = linha.split()  # Separa a linha por espaços
        if len(partes) >= 3:  # Verifica se a linha tem pelo menos 3 elementos
          bairro = obter_nome_completo(partes)
          if bairro == "VILA MEDEIROS":
            n = partes[-3]
            inc = '0'
          else:
            n = partes[-2]
            inc = partes[-1]
          dados_extraidos.append((bairro, inc, n))

      # Salva os dados extraídos em um arquivo de texto
      dados_json = []
      for bairro, inc, n in dados_extraidos:
        sinc = inc.replace(",", ".")
        for linha in bairros_validos_latLong:
          if linha["Bairro"] == bairro:
            lat = linha["LAT"]
            long = linha["LONG"]
            reg = linha["Regiao"]
            break

        if bairro in bairros_validos:
          dados_json.append(
            {
              "Regiao": reg,
              "Bairro": bairro,
              "INC": float(sinc),  # Converte INC para float
              "Casos": int(n),  # Converte Casos para int
              "LAT": lat,
              "LONG": long
            }
          )

      retorno = json.dumps(dados_json).replace('\"','').replace('"[','[').replace(']"',']')
      return retorno

  except FileNotFoundError:
    print(f"Arquivo '{caminho_arquivo}' não encontrado!")
  except IndexError:
    print(f"O arquivo PDF não possui a página {paginas}.")

def obter_nome_completo(partes):
  
  nome_completo = ""
  for parte in partes:
    if not parte.isdigit():  # Verifica se a parte não é um número
      nome_completo += parte + " "
    else:
      # Se encontrar um número, para a concatenação do bairro
      break
  return nome_completo.strip()  # Remove espaços em branco no início e no final

bairros_validos = [
    "BOM RETIRO", "CONSOLAÇÃO", "SANTA CECILIA", "BELA VISTA", "CAMBUCI",
    "LIBERDADE", "REPÚBLICA", "SÉ", "CIDADE TIRADENTES", "ERMELINO",
    "PONTE RASA", "GUAIANASES", "LAJEADO", "ITAIM PAULISTA", "VILA CURUÇA",
    "CIDADE LIDER", "ITAQUERA", "JOSÉ BONIFÁCIO", "PARQUE DO CARMO", "IGUATEMI",
    "SÃO MATEUS", "SÃO RAFAEL", "JARDIM HELENA", "SÃO MIGUEL", "VILA JACUI",
    "CACHOEIRINHA", "CASA VERDE", "LIMÃO", "BRASILANDIA", "FREGUESIA DO O",
    "JAÇANÃ", "TREMEMBÉ", "ANHANGUERA", "PERUS", "JARAGUA", "PIRITUBA",
    "SÃO DOMINGOS", "MANDAQUI", "SANTANA", "TUCURUVI", "VILA GUILHERME",
    "VILA MARIA", "VILA MEDEIROS", "BUTANTA", "MORUMBI", "RAPOSO TAVARES",
    "RIO PEQUENO", "VILA SONIA", "ALTO DE PINHEIROS", "BARRA FUNDA",
    "ITAIM BIBI", "JAGUARA", "JAGUARE", "JARDIM PAULISTA", "LAPA",
    "PERDIZES", "PINHEIROS", "VILA LEOPOLDINA", "CURSINO", "IPIRANGA",
    "SACOMÃ", "AGUA RASA", "ARICANDUVA", "BELÉM", "BRAS", "CARRÃO",
    "MOOCA", "PARI", "TATUAPÉ", "VILA FORMOSA", "ARTUR ALVIM", "CANGAÍBA",
    "PENHA", "VILA MATILDE", "JABAQUARA", "MOEMA", "SAUDE", "VILA MARIANA",
    "SÃO LUCAS", "SAPOPEMBA", "VILA PRUDENTE", "CAMPO LIMPO", "CAPÃO REDONDO",
    "VILA ANDRADE", "CIDADE DUTRA", "GRAJAÚ", "SOCORRO", "JARDIM ANGELA",
    "JARDIM SÃO LUIZ", "MARSILAC", "PARELHEIROS", "CAMPO BELO", "CAMPO GRANDE",
    "CIDADE ADEMAR", "PEDREIRA", "SANTO AMARO"
]

bairros_validos_latLong = [
    {"Regiao":"CENTRO", "Bairro": "BOM RETIRO", "LAT": -23.5255, "LONG": -46.6424},
    {"Regiao":"CENTRO", "Bairro": "CONSOLAÇÃO", "LAT": -23.5529, "LONG": -46.6609},
    {"Regiao":"CENTRO", "Bairro": "SANTA CECILIA", "LAT": -23.5379, "LONG": -46.6538},
    {"Regiao":"CENTRO", "Bairro": "BELA VISTA", "LAT": -23.5603, "LONG": -46.6486},
    {"Regiao":"CENTRO", "Bairro": "CAMBUCI", "LAT": -23.5649, "LONG": -46.6227},
    {"Regiao":"CENTRO", "Bairro": "LIBERDADE", "LAT": -23.5563, "LONG": -46.6359},
    {"Regiao":"CENTRO", "Bairro": "REPÚBLICA", "LAT": -23.5460, "LONG": -46.6434},
    {"Regiao":"CENTRO", "Bairro": "SÉ", "LAT": -23.5505, "LONG": -46.6333},
    {"Regiao":"LESTE", "Bairro": "CIDADE TIRADENTES", "LAT": -23.5828, "LONG": -46.4033},
    {"Regiao":"LESTE", "Bairro": "ERMELINO", "LAT": -23.4918, "LONG": -46.4822},
    {"Regiao":"LESTE", "Bairro": "PONTE RASA", "LAT": -23.5101, "LONG": -46.4801},
    {"Regiao":"LESTE", "Bairro": "GUAIANASES", "LAT": -23.5565, "LONG": -46.4167},
    {"Regiao":"LESTE", "Bairro": "LAJEADO", "LAT": -23.5295, "LONG": -46.4157},
    {"Regiao":"LESTE", "Bairro": "ITAIM PAULISTA", "LAT": -23.5016, "LONG": -46.3995},
    {"Regiao":"LESTE", "Bairro": "VILA CURUÇA", "LAT": -23.5066, "LONG": -46.4182},
    {"Regiao":"LESTE", "Bairro": "CIDADE LIDER", "LAT": -23.5639, "LONG": -46.4508},
    {"Regiao":"LESTE", "Bairro": "ITAQUERA", "LAT": -23.5425, "LONG": -46.4374},
    {"Regiao":"LESTE", "Bairro": "JOSÉ BONIFÁCIO", "LAT": -23.5407, "LONG": -46.4242},
    {"Regiao":"LESTE", "Bairro": "PARQUE DO CARMO", "LAT": -23.5525, "LONG": -46.4354},
    {"Regiao":"LESTE", "Bairro": "IGUATEMI", "LAT": -23.6058, "LONG": -46.4593},
    {"Regiao":"LESTE", "Bairro": "SÃO MATEUS", "LAT": -23.5983, "LONG": -46.4569},
    {"Regiao":"LESTE", "Bairro": "SÃO RAFAEL", "LAT": -23.6247, "LONG": -46.4648},
    {"Regiao":"LESTE", "Bairro": "JARDIM HELENA", "LAT": -23.4826, "LONG": -46.4268},
    {"Regiao":"LESTE", "Bairro": "SÃO MIGUEL", "LAT": -23.5010, "LONG": -46.4249},
    {"Regiao":"LESTE", "Bairro": "VILA JACUI", "LAT": -23.5045, "LONG": -46.4487},
    {"Regiao":"NORTE", "Bairro": "CACHOEIRINHA", "LAT": -23.4488, "LONG": -46.6646},
    {"Regiao":"NORTE", "Bairro": "CASA VERDE", "LAT": -23.5080, "LONG": -46.6573},
    {"Regiao":"NORTE", "Bairro": "LIMÃO", "LAT": -23.5052, "LONG": -46.6758},
    {"Regiao":"NORTE", "Bairro": "BRASILANDIA", "LAT": -23.4480, "LONG": -46.6907},
    {"Regiao":"NORTE", "Bairro": "FREGUESIA DO O", "LAT": -23.4852, "LONG": -46.6944},
    {"Regiao":"NORTE", "Bairro": "JAÇANÃ", "LAT": -23.4662, "LONG": -46.5759},
    {"Regiao":"NORTE", "Bairro": "TREMEMBÉ", "LAT": -23.4673, "LONG": -46.6206},
    {"Regiao":"NORTE", "Bairro": "ANHANGUERA", "LAT": -23.4200, "LONG": -46.7800},
    {"Regiao":"NORTE", "Bairro": "PERUS", "LAT": -23.4085, "LONG": -46.7456},
    {"Regiao":"NORTE", "Bairro": "JARAGUA", "LAT": -23.4452, "LONG": -46.7375},
    {"Regiao":"NORTE", "Bairro": "PIRITUBA", "LAT": -23.4875, "LONG": -46.7423},
    {"Regiao":"NORTE", "Bairro": "SÃO DOMINGOS", "LAT": -23.4850, "LONG": -46.7450},
    {"Regiao":"NORTE", "Bairro": "MANDAQUI", "LAT": -23.4704, "LONG": -46.6398},
    {"Regiao":"NORTE", "Bairro": "SANTANA", "LAT": -23.5007, "LONG": -46.6289},
    {"Regiao":"NORTE", "Bairro": "TUCURUVI", "LAT": -23.4803, "LONG": -46.6031},
    {"Regiao":"NORTE", "Bairro": "VILA GUILHERME", "LAT": -23.5163, "LONG": -46.6175},
    {"Regiao":"NORTE", "Bairro": "VILA MARIA", "LAT": -23.5101, "LONG": -46.6012},
    {"Regiao":"NORTE", "Bairro": "VILA MEDEIROS", "LAT": -23.4908, "LONG": -46.5887},
    {"Regiao":"OESTE", "Bairro": "BUTANTA", "LAT": -23.5612, "LONG": -46.7319},
    {"Regiao":"OESTE", "Bairro": "MORUMBI", "LAT": -23.5965, "LONG": -46.7171},
    {"Regiao":"OESTE", "Bairro": "RAPOSO TAVARES", "LAT": -23.5915, "LONG": -46.7808},
    {"Regiao":"OESTE", "Bairro": "RIO PEQUENO", "LAT": -23.5801, "LONG": -46.7428},
    {"Regiao":"OESTE", "Bairro": "VILA SONIA", "LAT": -23.5995, "LONG": -46.7399},
    {"Regiao":"OESTE", "Bairro": "ALTO DE PINHEIROS", "LAT": -23.5495, "LONG": -46.7128},
    {"Regiao":"OESTE", "Bairro": "BARRA FUNDA", "LAT": -23.5258, "LONG": -46.6674},
    {"Regiao":"OESTE", "Bairro": "ITAIM BIBI", "LAT": -23.5843, "LONG": -46.6781},
    {"Regiao":"OESTE", "Bairro": "JAGUARA", "LAT": -23.5072, "LONG": -46.7552},
    {"Regiao":"OESTE", "Bairro": "JAGUARE", "LAT": -23.5275, "LONG": -46.7492},
    {"Regiao":"OESTE", "Bairro": "JARDIM PAULISTA", "LAT": -23.5674, "LONG": -46.6564},
    {"Regiao":"OESTE", "Bairro": "LAPA", "LAT": -23.5216, "LONG": -46.7048},
    {"Regiao":"OESTE", "Bairro": "PERDIZES", "LAT": -23.5372, "LONG": -46.6806},
    {"Regiao":"OESTE", "Bairro": "PINHEIROS", "LAT": -23.5617, "LONG": -46.6917},
    {"Regiao":"OESTE", "Bairro": "VILA LEOPOLDINA", "LAT": -23.5309, "LONG": -46.7378},
    {"Regiao":"SUDESTE", "Bairro": "CURSINO", "LAT": -23.6329, "LONG": -46.6123},
    {"Regiao":"SUDESTE", "Bairro": "IPIRANGA", "LAT": -23.5893, "LONG": -46.6069},
    {"Regiao":"SUDESTE", "Bairro": "SACOMÃ", "LAT": -23.6025, "LONG": -46.6023},
    {"Regiao":"SUDESTE", "Bairro": "AGUA RASA", "LAT": -23.5614, "LONG": -46.5732},
    {"Regiao":"SUDESTE", "Bairro": "ARICANDUVA", "LAT": -23.5796, "LONG": -46.5118},
    {"Regiao":"SUDESTE", "Bairro": "BELÉM", "LAT": -23.5404, "LONG": -46.5887},
    {"Regiao":"SUDESTE", "Bairro": "BRAS", "LAT": -23.5455, "LONG": -46.6158},
    {"Regiao":"SUDESTE", "Bairro": "CARRÃO", "LAT": -23.5501, "LONG": -46.5372},
    {"Regiao":"SUDESTE", "Bairro": "MOOCA", "LAT": -23.5601, "LONG": -46.5979},
    {"Regiao":"SUDESTE", "Bairro": "PARI", "LAT": -23.5331, "LONG": -46.6148},
    {"Regiao":"SUDESTE", "Bairro": "TATUAPÉ", "LAT": -23.5402, "LONG": -46.5749},
    {"Regiao":"SUDESTE", "Bairro": "VILA FORMOSA", "LAT": -23.5667, "LONG": -46.5462},
    {"Regiao":"SUDESTE", "Bairro": "ARTUR ALVIM", "LAT": -23.5403, "LONG": -46.4842},
    {"Regiao":"SUDESTE", "Bairro": "CANGAÍBA", "LAT": -23.5017, "LONG": -46.5115},
    {"Regiao":"SUDESTE", "Bairro": "PENHA", "LAT": -23.5213, "LONG": -46.5289},
    {"Regiao":"SUDESTE", "Bairro": "VILA MATILDE", "LAT": -23.5293, "LONG": -46.5232},
    {"Regiao":"SUDESTE", "Bairro": "JABAQUARA", "LAT": -23.6526, "LONG": -46.6505},
    {"Regiao":"SUDESTE", "Bairro": "MOEMA", "LAT": -23.5971, "LONG": -46.6628},
    {"Regiao":"SUDESTE", "Bairro": "SAUDE", "LAT": -23.6163, "LONG": -46.6412},
    {"Regiao":"SUDESTE", "Bairro": "VILA MARIANA", "LAT": -23.5845, "LONG": -46.6368},
    {"Regiao":"SUDESTE", "Bairro": "SÃO LUCAS", "LAT": -23.6002, "LONG": -46.5181},
    {"Regiao":"SUDESTE", "Bairro": "SAPOPEMBA", "LAT": -23.6044, "LONG": -46.5094},
    {"Regiao":"SUDESTE", "Bairro": "VILA PRUDENTE", "LAT": -23.5827, "LONG": -46.5769},
    {"Regiao":"SUL", "Bairro": "CAMPO LIMPO", "LAT": -23.6486, "LONG": -46.7594},
    {"Regiao":"SUL", "Bairro": "CAPÃO REDONDO", "LAT": -23.6713, "LONG": -46.7794},
    {"Regiao":"SUL", "Bairro": "VILA ANDRADE", "LAT": -23.6256, "LONG": -46.7363},
    {"Regiao":"SUL", "Bairro": "CIDADE DUTRA", "LAT": -23.7121, "LONG": -46.7001},
    {"Regiao":"SUL", "Bairro": "GRAJAÚ", "LAT": -23.7858, "LONG": -46.6659},
    {"Regiao":"SUL", "Bairro": "SOCORRO", "LAT": -23.6934, "LONG": -46.7196},
    {"Regiao":"SUL", "Bairro": "JARDIM ANGELA", "LAT": -23.7126, "LONG": -46.7683},
    {"Regiao":"SUL", "Bairro": "JARDIM SÃO LUIZ", "LAT": -23.6836, "LONG": -46.7378},
    {"Regiao":"SUL", "Bairro": "MARSILAC", "LAT": -23.9216, "LONG": -46.6938},
    {"Regiao":"SUL", "Bairro": "PARELHEIROS", "LAT": -23.8344, "LONG": -46.7276},
    {"Regiao":"SUL", "Bairro": "CAMPO BELO", "LAT": -23.6226, "LONG": -46.6763},
    {"Regiao":"SUL", "Bairro": "CAMPO GRANDE", "LAT": -23.6852, "LONG": -46.7056},
    {"Regiao":"SUL", "Bairro": "CIDADE ADEMAR", "LAT": -23.6695, "LONG": -46.6588},
    {"Regiao":"SUL", "Bairro": "PEDREIRA", "LAT": -23.7086, "LONG": -46.7067},
    {"Regiao":"SUL", "Bairro": "SANTO AMARO", "LAT": -23.6465, "LONG": -46.7195}
]


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/boletim')
def get_boletim():
  dados_json = baixar_boletim_mais_recente()
  return jsonify(dados_json)

if __name__ == '__main__':
  app.run(debug=True)