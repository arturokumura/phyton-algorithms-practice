'''Faça uma função que a partir dos parâmetros inteiros M e N, retorne uma
matriz de M linhas e N colunas do tipo Real, com elementos fornecidos pelo
usuário. Utilize a função Real(n) que você criou no exercício 3 para validar sua
entrada antes de convertê-la com float() e adicioná-la à matriz'''
def Real(n):
    numeros = "0123456789"
    if n == "":
        return False
    if n[0] == "-":
        n = n[1:]
    if n == "":
        return False
    cont = 0
    for c in n:
       if c == '.':
           cont += 1
       if cont > 1:
            return False
       elif c not in numeros and c != '.':
           return False
    return True

def matriz(m,n):
    mat = []
    for i in range(m):
        linha = []
        for j in range(n):
            v = input("Valor: ")
            while not Real(v):
                print("Valor inválido!")
                v = input("Valor novamente: ")
            linha.append(v)
        mat.append(linha)
    for linhat in mat:
        for elemento in linhat:
            print(elemento, end = " ")
        print()

matriz(2,2)
