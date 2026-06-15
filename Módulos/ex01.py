import string
def ValidaInteiroPositivo(nro):
    if nro[0] == '+':
        nro = nro[1:]
    for i in nro:
        if i not in string.digits:
            return False
    return True

def ValidaInteiro(nro):
    cont = 0
    if nro[0] in '+-':
        nro = nro[1:]
    for i in nro:
        if i == '.':
            cont += 1
        else:
            if i not in string.digits:
                return False
    if cont == 0:
        return True
    else:
        return False

def NumeroReal(nro):
    if nro[0] in '+-':
        nro = nro[1:]
    cont_ponto = 0

    for i in nro:
        if i == '.':
            cont_ponto += 1
        elif i not in string.digits:
            return False

    if cont_ponto <= 1:
        return True
    return False
