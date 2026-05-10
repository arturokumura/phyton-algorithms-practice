'''9. Escreva um programa que leia duas matrizes retangulares A e B, com dimensões
MxN e NxP, respectivamente, e calcule o produto entre elas.'''
print("------Matriz A-------")
m = int(input("Linhas: "))
n = int(input("Colunas: "))
matriza = []
for i in range(m):
    linhaa = []
    for j in range(n):
        a = int(input(f"Valor [i][j]: "))
        linhaa.append(a)
    matriza.append(linhaa)

print("-------Matriz B------")
p = int(input("Colunas: "))
matrizb = []
for i in range(n):
    linhab = []
    for j in range(p):
        b = int(input(f"Valor [i][j]: "))
        linhab.append(b)
    matrizb.append(linhab)

# Cria a matriz resultado (M x P)
matrizc = []
for i in range(m):
    linha = []
    for j in range(p):
        linha.append(0)
    matrizc.append(linha)

# Multiplicação das matrizes
for i in range(m):
    for j in range(p):
        soma = 0
        for k in range(n):
           soma = soma + matriza[i][k] * matrizb[k][j]
        matrizc[i][j] = soma

for linhac in matrizc:
    for elemento in linhac:
        print(elemento, end = " ")
    print()
