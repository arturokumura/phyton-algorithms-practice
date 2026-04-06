'''● Faça um programa que leia uma String e escreva:
○ O número de caracteres que a string contém
○ Caractere por caractere, utilizando laço de repetição
○ Caractere por caractere, porém na ordem inversa, utilizando laço de repetição
'''

texto = input("Digite um texto: ")
contador = 0
invertida= ""
print("Caracteres: ")
for c in texto:
    contador += 1
    print(c)
print(f"Numero de caracteres: {contador}")

#Caracteres invertidos
print("Caracteres invertidos: ")
for i in range(len(texto)-1, -1, -1):
    print(texto[i])



