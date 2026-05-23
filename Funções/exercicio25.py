'''Faça uma função que a partir de um parâmetro inteiro N, retorne uma lista de N
elementos do tipo Inteiro, com elementos fornecidos pelo usuário. Utilize a
função Inteiro(n) que você criou no exercício 2 para validar seu valor de entrada
antes de convertê-lo com int() e adicioná-lo à lista.'''
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
print(list(3))
