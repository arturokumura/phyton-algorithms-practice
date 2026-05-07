'''15. Faça um programa que permita que o usuário digite várias strings. A digitação
termina quando o usuário digitar “fim”. Armazene as strings em uma lista. Ao final,
exiba qual é a string maior e qual e a string menor (em quantidade de caracteres).'''
s = input("Digite uma string: ")
lista =[]

while s.lower() != "fim":
    lista.append(s)
    s = input("Digite uma string: ")

maior = lista[0]
menor = []
for i in range(len(lista)):
    if len(lista[i]) > len(maior):
        maior = lista[i]
    if len(lista[i]) < len(maior):
        menor = lista[i]
print(maior)
print(menor)
