'''● Faça um programa que leia uma a entrada de um número inteiro positivo ou
negativo e mostre a quantidade de dígitos desse número.'''

num = input("Digite um numero inteiro (Informe se o número é positivo ou negativo(+/-)): ")

# Verifica o sinal
if num[0] == '-':
    natureza_numero = "negativo"
    num = num[1:]  # remove o sinal
elif num[0] == '+':
    natureza_numero = "positivo"
    num = num[1:]  
else:
    natureza_numero = "positivo"

# Conta os dígitos
contador = 0
for i in num:
    contador += 1

print(f"O número {num} é {natureza_numero}")
print(f"Total de digitos: {contador}")
