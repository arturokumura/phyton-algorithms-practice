'''Elabore uma função que receba como parâmetros uma matriz A de elementos
inteiros, de dimensões m linhas x n colunas, fornecidas pelo usuário e um valor Z
que será o fator multiplicador de cada elemento da matriz. Retorne a matriz
MULT(mxn), que conterá o resultado da multiplicação dos elementos da matriz
pelo fator multiplicador (Aij*Z). O programa principal deve fazer a leitura da
matriz e do fator, mostrar a matriz A(mxn), o fator Z e a matriz MULT(mxn).'''
def matriz(A,M,N,Z):
    res = []
    for i in range(M):
        linhar = []
        for j in range(N):
            r = A[i][j] * Z
            linhar.append(r)
        res.append(linhar)
    for linha in res:
        for elemento in linha:
            print(elemento, end = " ")
        print()

m = 2
n = 2
z = 2
a = []
for i in range(m):
    linhaa =[]
    for j in range(n):
        v = int(input("Valor: "))
        linhaa.append(v)
    a.append(linhaa)
matriz(a,m,n,z)

