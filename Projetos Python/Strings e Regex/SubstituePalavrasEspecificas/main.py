""" Substituindo palavras específicas
 Próxima Atividade

Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.

Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as alterações aplicadas.

Exemplo de Entrada:

Digite o texto a ser revisado: O dia está bom, tudo está bom.`
Qual palavra deseja substituir? bom
Qual a nova palavra? ótimo

Saída esperada:

O dia está ótimo, tudo está ótimo.

"""
import re
def main():
    print("*** Substituindo palavras específicas ***\n")
    texto = input("Digite o texto a ser revisado: ")
    palavra_substituida = input("Qual palavra deseja substituir? ")
    nova_palavra = input("Qual a nova palavra? ")
    print(substituir_palavras(texto, palavra_substituida, nova_palavra))

def substituir_palavras(texto, palavra_substituida, nova_palavra):
    """
    Solução 1:
    Utilizamos re.sub() para substituir todas as ocorrências da palavra 
    palavra_substituida por nova_palavra no texto.
    """
    # return re.sub(palavra_substituida, nova_palavra, texto)


    """
    Solução 2
    Podemos explorar o método re.sub() para substituir todas as ocorrências da palavra 
    antiga pela palavra nova. Utilizamos ainda a regex \b para garantir que apenas 
    palavras completas sejam substituídas, evitando alterações em partes de palavras maiores (como "bombom").
    """
    return re.sub(r'\b' + palavra_substituida + r'\b', nova_palavra, texto)

if __name__ == "__main__":
    main()