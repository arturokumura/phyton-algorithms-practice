'''Faça uma função recursiva em Python que receba 2 parâmetros: uma string e uma letra. A
função deve remover somente a última ocorrência da letra na string. Não é permitido o uso de
funções que não sejam da sua autoria. Letras maiúsculas e minúsculas são tratadas como
diferentes.
Exemplo: func('Arara', 'r')
Saída: Araa '''
def remover(s,x,flag = False):
    if len(s) == 0:
        return  ""
    else:
        if s[-1] == x and not flag:
            return remover(s[:-1],x,True)
        else:
            return s[-1] + remover(s[:-1],x,flag)
frase = "Arara"
print(remover(frase,'r'))
