'''Faça um programa que leia uma frase e imprima o número de palavras que a
frase contém.
'''
contador  = 1
frase = input("Digite a frase: ")
for c in frase:
    if c == " ":  
      contador += 1
print(contador)
