'''● Faça um programa que leia uma frase e mostre a quantidade total de uma letra
informada pelo usuário presente na frase.
● Entradas: frase e letra a ser contada'''

#Entrada
frase = input("Digite a frase: ")
letra = input("Letra a ser contada: ")
contador = 0

for c in frase:
    if c == letra:
        contador += 1
print (f"A letra {letra} está presente {contador} vezes na frase") 
