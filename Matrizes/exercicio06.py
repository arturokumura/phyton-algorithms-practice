'''6. Faça um programa que leia uma matriz de ordem MxN (M e N informados pelo
usuário) e mostre sua matriz transposta em formato matricial.'''
m = int(input("Linhas: "))
n = int(input("Colunas: "))
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        v = int(input(f"Valor [i][j]: "))
        linha.append(v)
    matriz.append(linha)

transposta = []
for i in range(m):
    linhat = []
    for j in range(n):
        c = matriz[j][i]
        linhat.append(c)
    transposta.append(linhat)

for linha in transposta:
    for elemento in linha:
        print(elemento, end = " ")
    print()
