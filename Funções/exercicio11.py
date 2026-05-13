'''Faça uma função que recebe como parâmetros a base e o expoente e retorna o
valor da potência. Não é permitido utilizar nenhuma função do Python para o
calculo da potência e nem o uso do operador **.'''
def potencia(b,p):
    soma = 1
    for i in range(p):
        soma = soma * b
    return soma

print("--------Potência---------")
base = int(input("Base: "))
pot = int(input("Potência: "))
print("Resultado: ", potencia(base,pot))
