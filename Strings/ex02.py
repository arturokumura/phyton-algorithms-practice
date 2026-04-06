'''Faça um programa que leia uma frase e imprima a quantidade de caracteres que
essa string contém, com exceção de espaços em branco.
'''

texto = input("Digite uma frase: ")
contador = 0
for c in texto:
    if c != " ":
        contador += 1
print(contador)
