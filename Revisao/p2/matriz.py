'''Faça uma função em Python que receba uma matriz quadrada de ordem impar como parâmetro
e retorne uma outra matriz com a coluna central trocada com a linha central. Dentro da função
você deve se certificar se a matriz é quadrada de ordem ímpar e se não for, retorne a matriz
original. Não é permitido o uso de funções que não sejam da sua autoria'''
def matriz(mat):
    l = len(mat)
    c = len(mat[0])
    if l % 2 !=0 or c % 2 != 0:
        for linhal in mat:
            for eleml in mat:
                print(eleml,end = " ")
            print()
    else:
        linha = []
        coluna = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i] == mat[l/2]:
                    linha.append(mat[i])
                elif mat[j] == mat[c/2]:
                    coluna.append(mat[j])
        print(linha)
        print(coluna)
m=3
n =3
mt = []
for i in range(m):
    linhat = []
    for j in range(n):
        v = int(input("V; "))
        linhat.append(v)
    mt.append(linhat)

matriz(mt)
