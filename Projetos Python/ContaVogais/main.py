#Mariana é professora de língua portuguesa e quer um programa que conte quantas 
#vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura 
#das palavras utilizadas.

#Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

def main():
    print("*** Contador de vogais ***\n")
    
    texto = input("Digite um texto: ")
    print(conta_vogais(texto))

def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return f"O texto contém {contador} vogais."

if __name__ == "__main__":
    main()    