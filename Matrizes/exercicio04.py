'''4. Faça um programa que leia a ordem de uma matriz quadrada e gere a matriz
identidade correspondente. Mostre a matriz gerada em formato matricial.'''
m = int(input("Indique a ordem da matriz: "))
matriz = []
for i in range(m):
    linha = []
    for j in range(m):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for elemento in matriz:
    for linha in elemento:
        print(linha, end = " ")
    print()

