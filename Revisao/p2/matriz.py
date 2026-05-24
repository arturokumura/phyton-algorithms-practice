'''Faça uma função em Python que receba uma matriz quadrada de ordem impar como parâmetro
e retorne uma outra matriz com a coluna central trocada com a linha central. Dentro da função
você deve se certificar se a matriz é quadrada de ordem ímpar e se não for, retorne a matriz
original. Não é permitido o uso de funções que não sejam da sua autoria'''
def troca_central(mat):

    linhas = len(mat)
    colunas = len(mat[0])

    if linhas != colunas or linhas % 2 == 0:
        return mat

    meio = linhas // 2

    for i in range(linhas):

        temp = mat[meio][i]

        mat[meio][i] = mat[i][meio]

        mat[i][meio] = temp

    return mat


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

resultado = troca_central(matriz)

for linha in resultado:

    for elem in linha:

        print(elem, end=" ")

    print()
