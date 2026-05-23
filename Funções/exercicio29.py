'''Faça uma função que receba 2 listas formadas por palavras (strings), o modo de
saída (U:união, I:intersecção, D:diferença) e retorne a lista resultante.'''
def conjuntos(l1,l2):
    s = input("Digite uma frase para lista 1: ")
    while s != "":
        l1.append(s)
        s = input("Digite uma frase para lista 1: ")
    s = input("Digite uma palavra para lista 2: ")    
    while s != "":
        l2.append(s)
        s = input("Digite uma frase para lista 2: ")

def uniao(l1,l2):
    l3 = []
    for x in l1:
        l3.append(x)
    for x in l2:
        l3.append(x)
    return l3

def intersec(l1,l2):
    l3 = []
    for a in l1:
        for b in l2:
            if a == b:
                l3.append(a)
    return l3

def diferenca(l1,l2):
    l3 = []
    for a in l1:
        achou = False
        for b in l2:
            if a == b:
                achou = True
        if not achou:
            l3.append(a)
    return l3

lista1 = []
lista2 = []
conjuntos(lista1,lista2)
opcao = input("Escolha U, I ou D: ")
while opcao.upper() != "U" and opcao.upper() != "I" and opcao.upper() != "D":
    opcao = input("Escolha novamente: ")
if opcao.upper() == "I":
    print(intersec(lista1,lista2))
elif opcao.upper() == "U":
    print(uniao(lista1,lista2))
elif opcao.upper() == "D":
    print(diferenca(lista1,lista2))
