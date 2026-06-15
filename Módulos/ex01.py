import string
def ValidaInteiroPositivo(nro):
    if nro[0] == '+':
        nro = nro[1:]
    for i in nro:
        if i not in string.digits:
            return False
    return True

def ValidaInteiro(
