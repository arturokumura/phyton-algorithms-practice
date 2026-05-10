'''5. Faça um programa que leia duas matrizes de mesma ordem MxN e mostre as duas
matrizes originais e a matriz resultante da soma dessas matrizes, em formato
matricial.'''
m = int(input("Linhas: "))
n = int(input("Coluna: "))
matriz_1 = []
matriz_2 = []

#Matriz 1
print("------Matriz 1-------")
for i in range(m):
    linha_1 = []
    for j in range(n):
        v1 = int(input(f"Informe o valor [i][j]: "))
        linha_1.append(v1)
    matriz_1.append(linha_1)
print("------Matriz 2-------")
#Matriz 2
for i in range(m):
    linha_2 = []
    for j in range(n):
        v2 = int(input(f"Informe o valor [i][j]: "))
        linha_2.append(v2)
    matriz_2.append(linha_2)

#Printar matrizes
print("------Matriz 1-------")    
for linha in matriz_1:
    for elemento_1 in linha:
        print(elemento_1, end = " ")
    print()

print("------Matriz 2-------")
for linha_2 in matriz_2:
    for elemento_2 in linha_2:
        print(elemento_2, end = " ")
    print()

#Soma
matriz_c = []
for i in range(m):
    linha_c = []
    for j in range(n):
        c = matriz_1[i][j] + matriz_2[i][j]
        linha_c.append(c)
    matriz_c.append(linha_c)

print("------SOMA-----")
for linha_c in matriz_c:
    for elemento_c in linha_c:
        print(elemento_c, end = " ")
    print()
