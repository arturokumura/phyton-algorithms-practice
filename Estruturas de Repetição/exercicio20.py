#Dado um número inteiro de qualquer tamanho (inteiro longo), fornecido pelo
#usuário via teclado, elabore um programa para determinar a soma dos dígitos que
#forem pares.

num = int(input("Digite um número: "))

pares = 0
if num == 0:
    pares = 0 
else:
    while num > 0:
        digito = num % 10 
        if digito % 2 == 0: 
            pares += digito
        num = num // 10 
print(f"A soma dos dígitos pares é: {pares}")
print("Fim")

