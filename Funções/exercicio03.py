'''Incremente o programa anterior, de forma a possibilitar a escolha do número de
caracteres delimitadores e também do caractere delimitador
○ Para isso, a função escreveLinha() deve receber como parâmetro o número de caracteres a ser
escrito e o tipo de caractere. Exemplo:
'''
def escreveLinha(n, char):
    s = ""
    for i in range(n):
        s += char
    print(s)

escreveLinha(5, '*')
print("Instituto Federal")
escreveLinha(3, '=')
