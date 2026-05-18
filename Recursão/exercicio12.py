'''Faça uma função recursiva para retornar o produto dos elementos de uma lista
de números inteiros'''
def prod(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] * prod(l[1:])

lista = [1,2,3,4,5]
print(prod(lista))
