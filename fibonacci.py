'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.
'''
#número informado pelo usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

#função que realiza a sequência de Fibonacci
def Sequencia(numero):
    #variáveis 
    a, b = 0, 1
    #enquanto o a for menor que o número informado
    while a < numero:
        #a 'fórmula' da sequência
        a, b = b, a + b
    #se o número informado for igual ao a -> o número informo pertence à sequência
    if a == numero:
        #imprimindo no console
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    #se o número informado for menor que a -> o número informado não pertence à sequência.
    elif a > numero:
        #imprimindo no console
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

#chamando a função
Sequencia(numero)
