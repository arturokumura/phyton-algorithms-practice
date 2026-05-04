'''2. Faça um programa que leia uma quantidade N que indica o número de pessoas. Após isso,
leia a sequência de N alturas dessas pessoas e ao final mostre a sequência, a menor altura e
sua posição na sequência.'''
N = int(input("Informe a quantidade de pessoas: "))
alturas = []
maior = 0
menor = 0
for i in range(N):
    altura = float(input("Informe a altura: "))
    alturas.append(altura)
print(alturas)

#Pegar maior numero
for c in alturas:
    if c > maior:
        maior = c

#Menor numero
for j in range(len(alturas)):
    if alturas[i] < maior:
        menor = alturas[i]
        pos = i + 1
print(f"Menor altura: {menor}")
print(f"Posição da menor altura: {pos}")
