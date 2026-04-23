"""
Ana precisa de um programa simples para gerenciar suas tarefas diárias. 
Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, 
visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

Exemplo de entrada:

1. Adicionar tarefa 
2. Visualizar tarefas 
3. Remover tarefa 
4. Sair
Escolha uma opção: 1
Copiar código
Saída esperada:

Digite a tarefa: Estudar Python
Tarefa adicionada!
Copiar código
Caso selecione a opção 2 ao adicionar uma tarefa:

Tarefas:
1. Estudar Python
Copiar código
Caso selecione a opção 3 com uma tarefa adicionada:

Digite o número da tarefa a ser removida: 1
Tarefa 'Estudar Python' removida!
Copiar código
Caso selecione a opção 3 sem uma tarefa adicionada:

Digite o número da tarefa a ser removida: Estudar Python
Erro: Nenhuma tarefa para remover.
Copiar código
Caso selecione a opção 3 com uma opção inválida:

Escolha uma opção: 3
Digite o número da tarefa a ser removida: ABC
Erro: Entrada inválida! Digite um número.
Copiar código
Caso selecione nenhuma das opções listadas:

Escolha uma opção: 5
Erro: Opção inválida! Escolha uma opção entre 1 e 4.
Copiar código
Caso selecione a opção 4:

Escolha uma opção: 4 
Saindo do gerenciador de tarefas. Até mais!
"""

def main():
    print("*** Gerenciador de tarefas ***\n")
    gerenciador_tarefas()

def gerenciador_tarefas():
    tarefas = []
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada!")
        elif opcao == "2":
            if len(tarefas) == 0:
                print("Nenhuma tarefa adicionada.")
            else:
                print("Tarefas:")
                for i in range(len(tarefas)):
                    print(f"{i + 1}. {tarefas[i]}")
        elif opcao == "3":
            if len(tarefas) == 0:
                print("Nenhuma tarefa para remover.")
            else:
                try:
                    numero = int(input("Digite o número da tarefa a ser removida: "))
                    if 1 <= numero <= len(tarefas):
                        tarefa = tarefas.pop(numero - 1)
                        print(f"Tarefa '{tarefa}' removida!")
                    else:
                        print("Número de tarefa inválido.")
                except ValueError:
                    print("Erro: Entrada inválida! Digite um número.")
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()  