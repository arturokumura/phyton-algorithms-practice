'''Faça uma função recursiva em Python que receba como parâmetros duas listas de números
inteiros. A função deve retornar a primeira lista sem os elementos que estão na segunda lista.
Não é permitido o uso de funções que não sejam da sua autoria.
Exemplo: func( [21, 9, 35, 9, 43, 7], [7, 9, 8])
Saída: [21, 35, 43]'''
def existe(num, lista):
    if len(lista) == 0:
        return False
    if lista[0] == num:
        return True

    return existe(num, lista[1:])


def remover(lista1, lista2):

    if len(lista1) == 0:
        return []

    if existe(lista1[0], lista2):

        return remover(lista1[1:], lista2)

    else:

        return [lista1[0]] + remover(lista1[1:], lista2)


l1 = [21, 9, 35, 9, 43, 7]
l2 = [7, 9, 8]

print(remover(l1, l2))
