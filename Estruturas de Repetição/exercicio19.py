#Dados números inteiros n, i e j, todos maiores do que zero, imprimir em ordem
#crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Por
#exemplo, para n = 6, i = 2 e j = 3 a saída deverá ser:
#0 2 3 4 6 8  total de 6 números

n = int(input("Quantos múltiplos?: "))
i = int(input("Múltiplo de: "))
j = int(input("Múltiplo de: "))

num = 0
contador = 0

for num in range(100000):  # limite alto só pra garantir
    if num % i == 0 or num % j == 0:
        print(num)
        contador += 1
    
    if contador == n:
        break
