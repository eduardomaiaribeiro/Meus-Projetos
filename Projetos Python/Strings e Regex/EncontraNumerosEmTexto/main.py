"""
Encontrando números em um texto

João é atendente em uma farmácia e precisa verificar se um cliente forneceu um 
número de receita válido em uma descrição. O número da receita é sempre o único 
número presente no texto fornecido pelo cliente. 
Ele quer um programa que extraia esse número diretamente e confirme se o texto 
está correto, sem a necessidade de trabalhar com listas ou loops.

Com base nesse cenário, crie um programa que receba um texto com uma descrição e 
exiba uma mensagem com o número encontrado.

Exemplo de Entrada:

Digite a descrição da receita: A receita 1087568 foi enviada pelo cliente.

Saída esperada:

O número da receita é: 1087568
"""

import re

def main():
    print("*** Encontrando números em um texto ***\n")
    descricao = input("Digite a descrição da receita: ")
    print(encontrar_numero(descricao))

def encontrar_numero(descricao):
    """
    Utilizamos re.findall() para capturar números no texto e acessamos diretamente 
    o número com o índice [0]. Esse valor é exibido como o número da receita.
    """
    numero = re.findall(r'\d+', descricao)[0]  
    return f"O número da receita é: {numero}"

if __name__ == "__main__":
    main()