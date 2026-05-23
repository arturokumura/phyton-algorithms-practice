'''Faça uma função que a partir dos parâmetros inteiros M e N, retorne uma
matriz de M linhas e N colunas do tipo Inteiro, com elementos fornecidos pelo
usuário. Utilize a função Inteiro(n) que você criou no exercício 2 para validar sua
entrada antes de convertê-la com int() e adicioná-la à matriz.'''
def Inteiro(n):
    numeros = "0123456789"
    if n == "":
        return False
    if n[0] == "-":
        n = n[1:]
    if n == "":
        return False

    for c in n:
        if c not in numeros:
            return False
    return True

def matriz(m,n):
    mat = []
    for i in range(m):
        linha = []
        for j in range(n):
            v = input("Valor: ")
            while not Inteiro(v):
                print("Valor inválido!")
                v = input("Valor novamente: ")
            linha.append(v)
        mat.append(linha)
    for linhat in mat:
        for elemento in linhat:
            print(elemento, end = " ")
        print()

matriz(2,2)
