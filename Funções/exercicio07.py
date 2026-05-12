'''Faça uma função que recebe um número inteiro e retorna a quantidade de dígitos
desse numero. Exemplo: -12478  5'''
def quantDig(num):
    cont = 0
    while num > 0:
        dig = num % 10
        cont += 1
        num = num // 10
    return cont

print("----------Quantidade de digitos de um numero--------")
n = int(input("Informe um número: "))
print("Número de digitos: ", quantDig(n))
