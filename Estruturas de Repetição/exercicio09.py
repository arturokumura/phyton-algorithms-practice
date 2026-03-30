N = int(input("Informe o numero do fatorial: "))

fat = 1

for i in range(1, N + 1):
        fat = fat * i   

print (f"O fatorial do número {N} é {fat}")
