'''Faça uma função que receba 2 listas de valores inteiros(faça a consistência
utilizando a função que você criou no exercício 2) como parâmetros e retorne a
lista DIFERENÇA. Obs.: DIFERENÇA: todos os elementos da lista 1 que NÃO estão
na lista 2.'''
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

def diferenca(l1,l2):
    l3 = []
    for x in l1:
        achou = False
        for i in range(len(l2)):
            if x == l2[i]:
                achou = True
    if achou == False:
         l3.append(x)
    return l3
lista1 = listas(3)
lista2 = listas(4)
print(diferenca(lista1,lista2))
      
