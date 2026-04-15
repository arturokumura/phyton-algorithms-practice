'''Substitua todas as vogais da string por um caractere especial (*), e todas as consoantes por um número
representando sua posição no alfabeto (a=1, b=2, ..., z=26).'''

s = input("Digite a frase: ")
vogais = "aeiou"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
resultado = ""
pos = 0

for i in range(len(s)):
    if s[i] in vogais:
        resultado += '*'
    else:
        for j in range(len(alfabeto)):
            if s[i] == alfabeto[j]:
                pos = j + 1
                resultado += str(pos)
print(resultado)
        
