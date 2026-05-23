'''Faça uma função que receba 2 listas de valores inteiros(faça a consistência
utilizando a função que você criou no exercício 2) como parâmetros e retorne a
lista INTERSECÇÃO. Obs.: INTERSECÇÃO= elementos presentes nas 2 listas
'''
def Inteiro(n):
    numeros = "0123456789"
    if n == "":
        return False
    if n[0] == "-":
        n = n[1:]
    if n == "":
        return False

    for c in n:
        if c not in numeros:
            return False
    return True
def listas(N):
    l = []
    for i in range(N):
        valor = input("Valor: ")
        while not Inteiro(valor):
            print("Valor invalido! Tente novamente")
            valor = input("valor: ")
        l.append(int(valor))
    return l


def intersec(l1,l2):
    l3 = []
    for a in l1:
        for b in l2:
            if a == b:
                l3.append(a)
    return l3
lista1 =listas(4)
lista2 = listas(4)
print(intersec(lista1,lista2))
            
