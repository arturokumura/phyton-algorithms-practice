'''. Faça uma função InteiroPositivo(n) que verifica se uma string de entrada pode
ser convertida em um número inteiro positivo. A função deve retornar True em
caso afirmativo e False caso contrário'''
def InteiroPositivo(num):

    if num == "":
        return False

    for c in num:
        if c < '0' or c > '9':
            return False

    if int(num) > 0:
        return True
    else:
        return False


n = input("Digite: ")
print(InteiroPositivo(n))
