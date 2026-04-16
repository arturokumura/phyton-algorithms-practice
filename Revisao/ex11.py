''' Implemente um algoritmo que inverta cada palavra em uma frase mantendo a ordem das palavras, considerando
pontuação. Exemplo: "Python é incrível!" → "nohtyP é levírcni!"'''

s = input("Digite a frase: ")
palavra = ""
resultado = ""
for c in s:
    if c != " " :
        palavra += c
    else:
        invertida = ""
        for i in range(len(palavra) -1, -1, -1):
            invertida += palavra[i]
        resultado += invertida + " "
        palavra = ""
if palavra != "":
    invertida = ""
    for i in range(len(palavra) -1, -1, -1):
        invertida += palavra[i]
    resultado += invertida
print(resultado)
