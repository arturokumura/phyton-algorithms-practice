'''7. Faça um programa que leia uma matriz quadrada e verifique se ela é simétrica.
Uma matriz é simétrica quando ela é igual à sua transposta. Mostre uma mensagem
amigável ao usuário.'''
m = int(input("Ordem da matriz: "))
matriz = []
for i in range(m):
    linha = []
    for j in range(m):
        v = int(input("Informe o valor [i][j]: "))
        linha.append(v)
    matriz.append(linha)

transp = []
for i in range(m):
    linhat = []
    for j in range(m):
        c = matriz[j][i]
        linhat.append(c)
    transp.append(linhat)

if matriz == transp:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
