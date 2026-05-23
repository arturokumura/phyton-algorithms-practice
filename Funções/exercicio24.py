'''Faça uma função que a partir de um parâmetro inteiro N, retorne uma lista de N
elementos do tipo Real, com elementos fornecidos pelo usuário. Utilize a função
Real(n) que você criou no exercício anterior para validar seu valor de entrada
antes de convertê-lo com float() e adicioná-lo à lista.'''
def Real(n):
    numeros = "0123456789"
    if n == "":
        return False
    if n[0] == "-":
        n = n[1:]
    if n == "":
        return False
    cont = 0
    for c in n:
       if c == '.':
           cont += 1
       if cont > 1:
            return False
       elif c not in numeros and c != '.':
           return False
    return True
def List(N):
    l = []
    valido = False
    for i in range(N):
        valor = input("Valor: ")
        while not Real(valor):
             print("Tente novamente!")
             valor = input("Valor: ")
        l.append(float(valor))
           
    return l

print(List(3))
