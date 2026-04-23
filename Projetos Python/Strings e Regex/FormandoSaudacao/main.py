""" Formatando uma saudação
 Próxima Atividade

Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes. Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade onde ele mora.

Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.

Exemplo de Entrada:

Digite o nome do cliente: Laura
Digite a cidade do cliente: Rio de Janeiro
Copiar código
Saída esperada:

Olá, Laura! Bem-vinda ao sistema da cidade de Rio de Janeiro.   
"""

def main():
    print("*** Formando saudação ***\n")
    nome = input("Digite o nome do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    print(formar_saudacao(nome, cidade))

def formar_saudacao(nome, cidade):
    return f"Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}."

if __name__ == "__main__":
    main()