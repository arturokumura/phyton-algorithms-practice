'''Elabore um algoritmo que calcule e escreva o valor da soma dos 50 primeiros termos da série:
S = 1000 - 997 + 994 - 991 + ...
 1 2 3 4'''

soma = 0
numerador = 1000
sinal = 1

for i in range(1, 51):  # denominador de 1 até 50
    soma += sinal * (numerador / i)
    numerador -= 3
    sinal *= -1  # alterna sinal

print(soma)
