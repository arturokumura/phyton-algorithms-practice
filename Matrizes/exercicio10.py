'''10. Faça um programa que leia duas matrizes quadradas (A e B) de ordem informada
pelo usuário e verifique se B é a matriz inversa de A. Mostre uma mensagem
amigável ao usuário.'''
m = int(input("Ordem das matrizes: "))
matriza = []
matrizb = []
for i in range(m):
    linhaa = []
    for j in range(m):
        a = int(input(f"Valor de [i][j]: "))
        linhaa.append(a)
    matriza.append(linhaa)

for i in range(m):
    linhab = []
    for j in range(m):
        b = int(input(f"Valor de [i][j]: "))
        linhab.append(b)
    matrizb.append(linhab)

matrizc = []
for i in range(m):
    linhac = []
    for j in range(m):
        linhac.append(0)
    matrizc.append(linhac)

# Multiplicação das matrizes
for i in range(m):
    for j in range(m):
        soma = 0
        for k in range(m):
           soma = soma + matriza[i][k] * matrizb[k][j]
        matrizc[i][j] = soma

# Mostra a matriz resultante
print("---- Produto A x B ----")
for linhac in matrizc:
    for elemento in linhac:
        print(elemento, end=" ")
    print()

inversa = True

for i in range(m):
    for j in range(m):
        if i == j:  # diagonal principal deve ser 1
            if matrizc[i][j] != 1:
                inversa = False
        else:       # fora da diagonal deve ser 0
            if matrizc[i][j] != 0:
                inversa = False

# Mensagem final
if inversa:
    print("A matriz B é a inversa da matriz A!")
else:
    print("A matriz B NÃO é a inversa da matriz A.")
