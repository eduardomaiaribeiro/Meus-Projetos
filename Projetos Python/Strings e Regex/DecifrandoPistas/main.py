""" Decifrando pistas com palavras-chave
 Próxima Atividade

Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.

Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

Exemplo de Entrada:

Digite a palavra-chave: Misterioso

Saída esperada:

Primeiras: Mis
Últimas: oso
"""

def main():
    print("*** Decifrando pistas com palavras-chave ***\n")
    palavra = input("Digite a palavra-chave: ")
    print(decifrar_pistas(palavra))

def decifrar_pistas(palavra):
    # Opção utilizando fatiamento
    return f"Primeiras: {palavra[:3]}\nÚltimas: {palavra[-3:]}"

if __name__ == "__main__":
    main()
