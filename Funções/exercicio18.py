'''Faça uma função que recebe uma lista de números reais e retorna a lista ordenada
do maior para o menor valor. Não é permitido o uso de qualquer função que não
seja da sua autoria'''
def ord(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1,i, -1):
            if numeros[j] > numeros[j-1]:
                x = numeros[j]
                numeros[j] = numeros[j-1]
                numeros[j-1] = x
    return numeros

lista = [23,4,7,5,1,4]
print(ord(lista))
                
