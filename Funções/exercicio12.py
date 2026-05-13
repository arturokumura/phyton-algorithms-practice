'''Faça uma função que recebe uma lista de números reais e retorna o valor da soma
de todos os números. Não é permitido o uso de qualquer função que não seja da
sua autoria.'''
def soma(l):
    soma = 0
    for c in l:
        soma += c
    return soma

print("----------Soma Lista------------")
n = int(input("Tamanho da lista: "))
lista = []
for i in range(n):
    v = int(input("Número: "))
    lista.append(v)
print("Soma da lista: " , soma(lista))
