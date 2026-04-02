n = int(input("Informe um número: "))
soma = 0
while(n != 0):
    d = n % 10
    soma += d - (n % 10)
n = n//10
print(soma)
