'''Faça uma função recursiva para contar a quantidade uma determinada letra em
uma string;'''
def contLetra(l,c):
    if len(l) == 0:
        return 0
    else:
        if l[0] == c:
            return 1 + contLetra(l[1:],c)
        else:
            return contLetra(l[1:],c)

frase = "abacaxi escola"
elemento = "a"
print(contLetra(frase,elemento))
