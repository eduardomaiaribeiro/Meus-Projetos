# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. 
# Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, 
# e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, 
# impedindo que o usuário forneça valores inválidos, como letras ou números fora do 
# intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita 
# que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior 
# ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor 
# inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random

def main():
    print("*** Jogo de adivinhar número ***\n")    
    print(jogo_adivinhar_numero())

def jogo_adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo!")
            elif palpite > numero_secreto:
                print("Muito alto!")
            else:
                return f"Parabéns! Você acertou em {tentativas} tentativas."
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()    