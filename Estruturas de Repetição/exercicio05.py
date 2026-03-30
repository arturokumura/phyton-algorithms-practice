#Soma dos numeros pares de 0 ate 100
soma = 0
for i in range (0, (100 + 1)):
    if( i % 2 == 0 ):
        soma += i
print(soma)
