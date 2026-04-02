#Dado um número inteiro de qualquer tamanho (inteiro longo), fornecido pelo
#usuário via teclado, elabore um programa para determinar a soma dos dígitos que
#estiverem em posições ímpares (da esquerda para a direita
n = int(input("Informe um número: "))
soma = 0
while(n != 0):
    d = n % 10
    soma += d - (n % 10)
n = n//10
print(soma)
