'''● Faça um programa que leia uma frase informada pelo usuário (incluindo espaços
em branco), conte a quantidade de espaços em branco e a quantidade de vezes
que aparecem as vogais a, e, i, o, u.'''

frase = input("Digite a frase: ")
vogais = "aeiouAEIOU"
espaco = " "
contador_espaco = 0
contador_vogais = 0

for c in frase:
    if c == espaco:
        contador_espaco += 1
    if c in vogais:
        contador_vogais += 1
print(f"Total de espaços e  branco: {contador_espaco}")
print(f"Total de vogais: {contador_vogais}")
