# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def main():
    print("*** Calculadora com tratamento de erros ***\n")
    calculadora()

def calculadora():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            print(f"Resultado: {numero1 + numero2}")
        elif operacao == "-":
            print(f"Resultado: {numero1 - numero2}")
        elif operacao == "*":
            print(f"Resultado: {numero1 * numero2}")
        elif operacao == "/":
            print(f"Resultado: {numero1 / numero2}")
        else:
            print("Operação inválida.")
    except ValueError:
        print("Erro: Digite um número válido.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

if __name__ == "__main__":
    main()