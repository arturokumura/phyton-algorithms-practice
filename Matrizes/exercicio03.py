'''3. Faça um programa que crie uma matriz MxM quadrada com números fornecidos
pelo usuário. Após isso imprima a diagonal principal dessa matriz e o valor de seu
traço.
'''
linhas = 2
coluna = 2
matriz = []
for i in range(linhas):
    linha = []
    for j in range(coluna):
        v = int(input(f"Valor [i][j]: "))
        linha.append(v)
    matriz.append(linha)


# Imprime a matriz
print("\nMatriz:")
for i in range(linhas):
    for j in range(coluna):
        print(matriz[i][j], end=" ")
    print()

#Diagonal e traço
diagonal = []
traco = 0

for i in range(linhas):
    for j in range(coluna):
        if i == j:
            diagonal.append(matriz[i][j])
            traco += matriz[i][j]
print(diagonal)
print(traco)
