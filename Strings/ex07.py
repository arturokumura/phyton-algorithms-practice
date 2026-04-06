'''● Faça um programa que leia uma frase e retire todas as ocorrência de uma letra
da frase
● Entradas: frase e letra a ser removida
'''
#Inicializações
frase = input("Digite uma frase: ")
letra = input("Letra a ser removida: ")
nova_frase = ""

#Laço "for"
for c in frase:
    if c != letra:
        nova_frase += c
print(nova_frase)
