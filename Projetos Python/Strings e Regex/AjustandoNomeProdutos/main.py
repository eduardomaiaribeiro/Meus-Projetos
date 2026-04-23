""" Ajustando nomes de produtos
 Próxima Atividade

Victor trabalha em um sistema de e-commerce e precisa organizar os nomes dos produtos que estão sendo cadastrados pelos lojistas. Esses nomes geralmente vêm com letras misturadas entre maiúsculas e minúsculas, além de espaços desnecessários no início e no final.

Ajude Victor a criar um programa que receba um nome de produto e o padronize, deixando todas as letras minúsculas e removendo os espaços extras.

Exemplo de Entrada:

Digite o nome do produto: ChocoLAte Branco

Saída esperada:

chocolate branco
"""

def main():
    print("*** Ajustando nomes de produtos ***\n")
    nome_produto = input("Digite o nome do produto: ")
    print(ajustar_nome_produto(nome_produto))

def ajustar_nome_produto(nome_produto):
    nome_produto = nome_produto.strip().lower()
    return nome_produto

if __name__ == "__main__":
    main()