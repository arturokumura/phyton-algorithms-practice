'''Faça uma função que recebe uma frase e retorna o numero de palavras que a
frase contém.'''
def numPalavra(s):
    achou = False
    cont = 0
    for i in range(len(s)):
        if s[i] != " " and not achou:
            cont += 1
            achou = True
        elif s[i] == " ":
            achou = False
    return cont

print("---------Numero de palavras--------")
frase = input("Digite a frase: ")
print("Número de palavras: ", numPalavra(frase)) 
