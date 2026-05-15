'''Crie uma função para retornar a quantidade de caracteres de
uma string.'''
def contcaract(s):
    if len(s) == 1:
        return 1
    else:
        return 1 + contcaract(s[1:])

print("-----------Contador de caractreres em uma string-----------")
frase = input("Digite uma frase: ")
print(contcaract(frase))
