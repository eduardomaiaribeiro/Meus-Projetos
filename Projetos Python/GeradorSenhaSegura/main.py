# Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. 
# Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, 
# uma minúscula, um número e um caractere especial. Exiba a senha gerada.

import random
import string

def main():
    print("*** Gerador de senha segura ***\n")
    
    print(gerar_senha_segura())

def gerar_senha_segura():
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation
    senha = []
    senha.append(random.choice(letras_maiusculas))
    senha.append(random.choice(letras_minusculas))
    senha.append(random.choice(numeros))
    senha.append(random.choice(caracteres_especiais))
    for i in range(8):
        senha.append(random.choice(letras_maiusculas + letras_minusculas + numeros + caracteres_especiais))
    random.shuffle(senha)
    return "Senha gerada: " + "".join(senha)

if __name__ == "__main__":
    main()    