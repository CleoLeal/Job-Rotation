'''
    Escreva um programa que inverta os caracteres de um string.

    IMPORTANTE:
    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser 
    previamente definida no código;
    b) Evite usar funções prontas, como, por exemplo, reverse;
'''

#solciitando a palavra
palavra = input('Digite uma palavra: ')

#função para reverter
def reverter_palavra(palavra):
    #variável para salvar a função
    palavra_revertida = ""

    #percorre a palavra
    for letra in palavra:
        #salva na variáveç
        palavra_revertida = letra + palavra_revertida
    #retorna a palavra
    return palavra_revertida

#mostra os resultados
palavra_revertida = reverter_palavra(palavra)
print("Palavra original:", palavra)
print("Palavra revertida:", palavra_revertida)
