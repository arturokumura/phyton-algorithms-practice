'''Faça uma função recursiva para eliminar os números pares de uma lista de
números inteiros;'''
def par(l):
    if len(l) == 0:
        return []
    else:
        if l[0] % 2 == 0:
            return par(l[1:])
        else:
            return  [l[0]] + par(l[1:])
    
lista = [1,2,3,4,5,6]
print(par(lista))
    
