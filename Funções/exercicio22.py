'''Faça uma função Inteiro(n) que verifica se a string de entrada constitui um
número inteiro (positivo ou negativo). A função deve retornar True em caso
afirmativo e False caso contrário'''
def Inteiro(n):
    numeros = "0123456789"
    if n == "":
        return False
    if n[0] == "-":
        n = n[1:]
    if n == "":
        return False

    for c in n:
        if c not in numeros:
            return False
    return True


print(Inteiro("123"))   
print(Inteiro("-123"))  
print(Inteiro("12b"))   
print(Inteiro("12.3"))   
