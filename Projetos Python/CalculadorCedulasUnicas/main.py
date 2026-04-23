"""
Contador de cédulas únicas


Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um 
programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado 
pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis 
são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas 
de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o 
valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar 
erros de entrada caso não seja digitado um valor numérico válido.

Exemplo de entrada:

Digite o valor do saque: 188  
Copiar código
Saída esperada:

Cédulas entregues:  
1 de R$ 100  
1 de R$ 50  
1 de R$ 20  
1 de R$ 10  
1 de R$ 5  
1 de R$ 2  
Copiar código
Caso faça um saque de valor não inválido (ímpar):

Erro: O valor deve ser múltiplo de 2.
"""

def main():
    print("*** Contador de cédulas únicas ***\n")
    calculadora_cedulas_unicas()

def calculadora_cedulas_unicas():
    try:
        valor = int(input("Digite o valor do saque: "))
        if valor % 2 != 0:
            print("Erro: O valor deve ser múltiplo de 2.")
        else:
            cedulas = [100, 50, 20, 10, 5, 2]
            for cedula in cedulas:
                if valor >= cedula:
                    quantidade = valor // cedula
                    print(f"{quantidade} de R$ {cedula}")
                    valor %= cedula
    except ValueError:
        print("Erro: Digite um valor válido.")

if __name__ == "__main__":
    main()