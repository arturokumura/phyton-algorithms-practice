'''16. Faça um programa que permita que o usuário digite várias strings. A digitação
termina quando o usuário digitar “fim”. Leia um caractere X e remova a primeira
ocorrência desse caractere em todas as strings da lista que possuírem tal caractere.
Caso uma string se transforme em string vazia, ela deve ser removida da lista.
Mostre a lista final'''
s = input("Informe uma string: ")

lista = []

while s.lower() != "fim":
    lista.append(s)
    s = input("Informe uma string: ")

x = input("Caractere: ")

lista_final = []

for palavra in lista:

    pos = -1

    # procura a posição da primeira ocorrência
    for i in range(len(palavra)):
        if palavra[i] == x and pos == -1:
            pos = i

    # se encontrou
    if pos != -1:
        nova = palavra[:pos] + palavra[pos+1:]
    else:
        nova = palavra

    # evita string vazia
    if nova != "":
        lista_final.append(nova)

print(lista_final)
