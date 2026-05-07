# matriz 3x4
linhas = 3
colunas = 4

# inicializa a matriz
mat = []

for i in range(linhas):  # linhas
    linha = []

    for j in range(colunas):  # colunas
        x = int(input(f"Informe o numero [{i}][{j}]: "))
        linha.append(x)

    mat.append(linha)

print(mat)
