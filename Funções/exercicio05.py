'''Faça uma função que recebe uma palavra e retorna o numero de letras que a
palavra possui. '''
def numLetras(s):
    cont = 0
    for c in s:
        cont += 1
    return cont

print("-------Contador de letras--------")
palavra = input("Informe uma palavra: ")
print("Número de letras da palavra", palavra, ": ", numLetras(palavra))
