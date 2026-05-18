'''Faça uma função recursiva para inverter uma string'''
def inverter(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + inverter(s[:-1])

frase = "bola alob"
print(inverter(frase))
