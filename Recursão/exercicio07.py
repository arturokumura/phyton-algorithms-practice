'''Crie uma função para exibir os algarismos de um número inteiro positivo
de forma invertida. Não é permitida a conversão para string. Exemplo:
326'''
def invert(num):
    if num < 10:
        print(num % 10)
    else:
        print(num % 10)
        invert(num//10)
print("------Numero-------")
numero  = int(input("Informe o numero: "))
invert(numero)
