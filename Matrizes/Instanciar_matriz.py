'''1. Faça um programa que leia 9 valores um a um e coloque em uma matriz 3x3. Após
isso, faça:
○ Imprima os 9 elementos no formato matricial
○ Imprima a soma total dos elementos
○ Imprima a soma dos elementos de cada linha'''

mat = []
linhas = 3
colunas = 3

for i in range(linhas):
    linha = []
    for j in range(colunas):
        x = int(input(f"Insira o valor de [{i}][{j}]: "))
        linha.append(x)
    mat.append(linha)

#Imprimir no formato matricial
for linha in mat:
    print(linha)

#Soma total dos elementos
soma = 0
for linha in mat:
    for elemento in linha:
        soma += elemento
print(f"Soma de todos os elementos: {soma}")

# Soma de cada linha
for linha in mat:
    soma_linha = 0
    for i in range(len(linha)):
        soma_linha += linha[i]
    print(f"Soma da linha {linha}: {soma_linha}")
