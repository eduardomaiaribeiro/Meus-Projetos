# Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. 
# Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que 
# encontre palavras que tenham mais de 10 letras e as exiba em destaque.

# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. 
# Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

def main():
    print("*** Identificador de palavras longas ***\n")
    
    texto = input("Digite um texto: ")
    print(identifica_palavras_longas(texto))

def identifica_palavras_longas(texto):
    palavras = texto.split()
    palavras_longas = []
    for palavra in palavras:
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    if len(palavras_longas) == 0:
        return "Nenhuma palavra longa encontrada."
    return f"Palavras longas: {', '.join(palavras_longas)}"

if __name__ == "__main__":
    main()    