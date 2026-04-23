""" 
Verificando o início e o fim de uma String

Renan está desenvolvendo um sistema que verifica se os links de sites parceiros 
começam com https:// e terminam com .com. Esses critérios são obrigatórios para 
que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize 
essa validação de forma automática.

Como você escreveria um programa que peça ao usuário uma URL e informe se ela é 
válida ou inválida?

Exemplo de Entrada:
Digite a URL para validação: https://monitorrenan.com

Saída esperada:
URL válida!

"""


def main():
    print("*** Verificando o início e o fim de uma String ***\n")
    url = input("Digite a URL para validação: ")
    print(validar_url(url))

def validar_url(url):
    if url.startswith("https://") and url.endswith(".com"):
        return "URL válida!"
    return "URL inválida!"

if __name__ == "__main__":
    main()  