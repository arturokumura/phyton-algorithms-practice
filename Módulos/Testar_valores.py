import ValidaValores

x = input("Digite um valor: ")
if ValidaValores.ValidaInteiroPositivo(x):
    x = int(x)
    print(x)
else:
    print("O número digitado não é um Inteiro Positivo")
