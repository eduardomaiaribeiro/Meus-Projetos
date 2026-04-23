
# Exemplos de Uso da OpenAI API

Esta pasta reúne notebooks e scripts práticos para explorar e experimentar recursos da API da OpenAI, incluindo geração de texto, chatbots, análise de dados, síntese e reconhecimento de voz, entre outros.

## 📚 Conteúdo

Principais arquivos e exemplos:

- **1-generate_text.ipynb** — Geração básica de textos com modelos OpenAI
- **2-chatbot.py / 2-chatbot_cor.py** — Chatbots simples e com interface colorida
- **3-fc_callingI.ipynb / 3-fc_callingII.py** — Funções chamadas por LLMs (function calling)
- **4-chat_finance.py / 4-chat_finance_st.py** — Chatbot para finanças, incluindo interface com Streamlit
- **5-assistant.ipynb / 6-assistant_dados.ipynb / 7-assistant_retrieval.ipynb** — Assistentes inteligentes e busca de informações
- **8-vc.ipynb** — Voice cloning e manipulação de voz
- **9-tts_stt.ipynb** — Text-to-Speech e Speech-to-Text
- **10-assistente_voz.py** — Assistente de voz interativo
- **generate_csv.py** — Geração automática de dados em CSV
- **test_yfincance.ipynb** — Testes de integração com dados financeiros

Arquivos auxiliares:
- **requirements.txt** — Dependências necessárias
- **sales_data.csv** — Exemplo de dados para análise
- **files/** — Pasta para arquivos de apoio

## 🚀 Como Executar

1. **Pré-requisitos:**
	- Python 3.x instalado
	- (Opcional) Ambiente virtual

2. **Instale as dependências:**
	```bash
	pip install -r requirements.txt
	```

3. **Configure sua chave de API:**
	- Crie um arquivo `.env` ou defina a variável de ambiente `OPENAI_API_KEY` com sua chave da OpenAI.

4. **Execute o notebook ou script desejado:**
	- Para notebooks:
	  ```bash
	  jupyter notebook NOME_DO_ARQUIVO.ipynb
	  ```
	- Para scripts:
	  ```bash
	  python NOME_DO_ARQUIVO.py
	  ```

## 🎯 Objetivo

Demonstrar, de forma prática, como integrar e utilizar os principais recursos da OpenAI API em projetos reais, servindo como referência e ponto de partida para novas aplicações.

---

