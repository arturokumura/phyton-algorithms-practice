#Crie uma função que exiba verticalmente uma string
def funct(s):
    if len(s) == 1:
        print(s)
    else:
        print(s[0])
        funct(s[1:])
    

print("-----------String-----------")
frase = input("Digite a frase: ")
funct(frase)
