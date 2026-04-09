'''● Faça um programa que leia um nome e mostre-o na tela na vertical e em formato
de escada'''

nome = input("Digite um nome: ")
escada = ""
for c in range(0, len(nome)):
    escada += nome[c]
    escada_maiuscula = escada.upper()
    print(escada_maiuscula)
