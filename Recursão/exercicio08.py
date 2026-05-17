'''Crie uma função para exibir os algarismos de um número positivo na
ordem correta. Não é permitida a conversão para string.'''
def alg(num):
    if num < 10:
        print(num)
    else:
        alg(num // 10)
        print(num%10)

print("--------Número------")
numero = int(input("Informe um numero: "))
alg(numero)
