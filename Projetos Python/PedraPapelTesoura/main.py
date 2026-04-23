# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. 
# O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. 
# Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

import random

def main():
    print("*** Pedra, papel e tesoura ***\n")
    print(pedra_papel_tesoura())

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    if usuario not in opcoes:
        return "Opção inválida."
    if usuario == computador:
        return "Empate."
    if (usuario == "pedra" and computador == "tesoura") or \
       (usuario == "papel" and computador == "pedra") or \
       (usuario == "tesoura" and computador == "papel"):
        return "Você venceu!"
    return "Computador venceu!"

if __name__ == "__main__":
    main()
