#Dado um número inteiro de qualquer tamanho (inteiro longo), fornecido pelo
#usuário via teclado, elabore um programa para determinar a quantidade de dígitos
#pares e a quantidade de dígitos ímpares

num = int(input("Informe o número: "))
pares = 0
impar = 0

while(num > 0):
    d = num % 10
    if ( d % 2 == 0):
        pares += 1
    else:
        impar += 1
    num = num // 10

print(f"Quantidade de pares : {pares}")
print(f"Quantidade de impares : {impar}")
