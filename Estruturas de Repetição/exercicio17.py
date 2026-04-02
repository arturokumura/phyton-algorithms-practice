#Faça um programa que receba dois números inteiros e mostre na tela os números
#inteiros que estão no intervalo compreendido por eles em ordem decrescente,
#incluindo-os. Considere que os números possam ser digitados em qualquer ordem

i = int(input("Digite o número que iniciará a sequência: "))
f = int(input("Dgiite o número que encerrará a sequência: "))

for n in range (i, (f-1) , -1):
    print(n)
