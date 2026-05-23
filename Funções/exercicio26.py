'''Faça uma função que receba 2 listas de valores inteiros (faça a consistência
utilizando a função que você criou no exercício 2) como parâmetros e retorne a
lista UNIÃO. Obs.: UNIÃO = concatenação sem repetição'''
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
def list(N):
    l = []
    for i in range(N):
        valor = input("Valor: ")
        while not Inteiro(valor):
            print("Valor invalido! Tente novamente")
            valor = input("valor: ")
        l.append(int(valor))
    return l

def uniao(l1,l2):
    l3 =[]
    for x in l1:
        if x not in l3:
            l3.append(x)
    for x in l2:
        if x not in l3:
            l3.append(x)
    return l3

l1 = list(3)
l2 = list(3)

print(uniao(l1,l2))
