'''2. Faça um programa que leia o número de linhas M de uma matriz e o número N de
colunas. Após isso, leia MxN valores e coloque-os na matriz. Por fim, imprima a
matriz em formato matricial'''
m = int(input("Linhas: "))
n = int(input("Colunas: "))
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        c = int(input(f"Valor [i][j]: "))
        linha.append(c)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end = " ")
    print()
                
