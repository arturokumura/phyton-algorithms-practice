'''5. Faça um programa que efetue a leitura de 15 elementos inteiros para uma lista A.
No final, apresente o total da soma de todos os elementos ímpares e pares.'''
A =[]
pares = 0
impares = 0

for i in range(15):
    num = float(input("Informe um número: "))
    A.append(num)

for c in A:
    if c % 2 == 0:
        pares += c
    else:
        impares += c
print(f"Soma dos ímpares: {impares}")
print(f"Soma dos pares: {pares}")
