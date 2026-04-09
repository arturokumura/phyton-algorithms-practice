'''● Faça um programa que leia um nome e mostre-o na tela de trás para frente com
letras maiúsculas somente.'''

nome = input("Informe o nome a ser transposto: ")
nome_invertido= ""
#Percorrer de tras pra frente
for i in range(len(nome) -1, -1, -1 ):
    nome_invertido = nome_invertido + nome[i]
    nome_maiusculo = nome_invertido.upper()
print(nome_maiusculo)
