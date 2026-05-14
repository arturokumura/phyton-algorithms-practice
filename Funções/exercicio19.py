''' Faça uma função que reconhece se uma string é um palíndromo. A função deve
considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” =
“A” e retornar True se é um palíndromo e False caso contrário. '''
def pal(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    if invertida.lower() == s.lower():
        return True
    else:
        return False

print("------------Palíndromo-------------")
frase = input("Digite a frase: ")
print(pal(frase))
