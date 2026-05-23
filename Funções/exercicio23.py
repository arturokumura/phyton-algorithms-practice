'''Faça uma função Real(n) que verifica se a string de entrada pode ser convertida
em um número real (positivo ou negativo). A função deve retornar True em caso
afirmativo e False caso contrário.
entrada: 123 saída: True entrada: 12b saída: False entrada: -12+34 saída: False
Entrada: -123 saída: True entrada:12.3 saída: True entrada: 12.34.56 saída: False'''
def Real(n):
    numeros = "0123456789"
    if n == "":
        return False
    if n[0] == "-":
        n = n[1:]
    if n == "":
        return False
    cont = 0
    for c in n:
       if c == '.':
           cont += 1
       if cont > 1:
            return False
       elif c not in numeros and c != '.':
           return False
    return True

num = input("Número: ")
print(Real(num))
