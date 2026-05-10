'''8. Faça um programa que leia duas matrizes de mesma ordem MxN e mostre as duas
matrizes originais e a matriz resultante A - B, em formato matricial'''
m = int(input("Linhas: "))
n = int(input("Colunas: "))

matriza = []
for i in range(m):
    linhaa = []
    for j in range(n):
        v = int(input(f"Valor de [i][j]: "))
        linhaa.append(v)
    matriza.append(linhaa)

matrizb = []
for i in range(m):
    linhab = []
    for j in range(n):
        b = int(input(f"Valor de [i][j]: "))
        linhab.append(b)
    matrizb.append(linhab)

matrizc = []
for i in range(m):
    linhac = []
    for j in range(n):
        c = matriza[i][j] - matrizb[i][j]
        linhac.append(c)
    matrizc.append(linhac)

for linhac in matrizc:
    for elemento in linhac:
        print(elemento, end = " ")
    print()
    
