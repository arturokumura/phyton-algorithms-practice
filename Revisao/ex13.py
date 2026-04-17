''' Implemente um algoritmo que substitua cada caractere de uma string pelo caractere que aparece n posições
depois no alfabeto (cifra de César), mantendo hierarquicamente/minúsculas e ignorando caracteres não-alfabéticos.'''

s = input("Digite a frase: ")
n = int(input("Informe quantas posições depois: "))

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos = 0
resultado = ""

for i in range(len(s)):
    achou = 0
    for j in range(len(alfabeto)):
        if s[i] == alfabeto[j]:
            pos = (j + n) % 26
            resultado += alfabeto[pos]
            achou = 1
            break
        elif s[i] == alfabeto_maiusculo[j]:
            pos = (j + n) % 26
            resultado += alfabeto_maiusculo[pos]
            achou = 1
            break
    if achou == 0:
        resultado += s[i]

print(resultado)
