''' Faça uma função que receba como parâmetros duas matrizes A e B de
elementos inteiros, de dimensões m linhas x n colunas, fornecidas pelo usuário
e retorne a matriz SOMA(mxn), que conterá o resultado da soma entre os
elementos de mesma posição(Aij+Bij). O programa principal deve fazer a leitura
das duas matrizes, mostrar a matriz A(mxn), a matriz B(mxn) e a matriz
SOMA(mxn)'''
def matriz(A,B):
    matc = []
    for i in range(m):
        linhac =[]
        for j in range(n):
            c = A[i][j] + B[i][j]
            linhac.append(c)
        matc.append(linhac)
    return matc

m = 2
n = 2
print("Matriz A")
mata = []
for i in range(m):
    linhaa =[]
    for j in range(n):
        v = int(input("Valor: "))
        linhaa.append(v)
    mata.append(linhaa)
print("Matriz B")
matb = []
for i in range(m):
    linhab =[]
    for j in range(n):
        v = int(input("Valor: "))
        linhab.append(v)
    matb.append(linhab)
for linha in mata:
    for elemento in linha:
        print(elemento, end = " ")
    print()
print()
print()
for linha in matb:
    for elemento in linha:
        print(elemento, end = " ")
    print()

print(matriz(mata,matb))
