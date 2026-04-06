#Dado um número inteiro de qualquer tamanho (inteiro longo), fornecido pelo
#usuário via teclado, elabore um programa para determinar a soma dos dígitos que
#estiverem em posições ímpares (da esquerda para a direita
num = int(input("Digite um numero: "))

# 1. Descobrir quantidade de dígitos
total_digitos = 0
temp = num
while temp > 0:
    temp //= 10
    total_digitos += 1

# 2. Processar da direita pra esquerda
contador = total_digitos
soma = 0

while num > 0:
    digito = num % 10
    
    if contador % 2 != 0:  # posição ímpar (da esquerda)
        soma += digito
    
    num //= 10
    contador -= 1

print(soma)
