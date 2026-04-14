'''7. Implemente um algoritmo que comprima sequências repetidas de caracteres em uma string, representando-as por
"caractere + número de repetições consecutivas". Exemplo: "aaabbc" vira "a3b2c1".'''

s = input("Digite os caracteres da string: ")

cont = 1

for i in range(len(s)):
    if i == len(s) - 1:
        print(s[i], cont , sep="", end="")
    elif s[i] == s[i+1]:
        cont += 1
    else:
        print(s[i], cont, sep="", end="")
        cont = 1
