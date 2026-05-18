'''Faça uma função recursiva para contar a quantidade um determinado elemento
em uma lista;'''
def cont(l,c):
    if len(l) == 1:
        if l[0] == c:
            return 1
        else:
            return 0
    else:
        if l[0] == c:
            return 1 + cont(l[1:],c)
        else:
            return cont(l[1:],c)

lista =[1,2,2,2,3,4,5]
elemento = 2
print(cont(lista,elemento))
