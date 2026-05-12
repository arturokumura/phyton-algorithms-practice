'''Faça uma função que recebe um número inteiro e retorna: 1 se o número é
positivo, -1 se o número é negativo ou 0 se o número for igual a zero.'''
def inteiro(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

num = int(input("Digite um numero: "))
res = inteiro(num)
print(res)
