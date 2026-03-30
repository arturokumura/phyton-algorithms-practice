n = int(input("Digite um número inteiro positivo: "))

a = 1
b = 1

for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo
