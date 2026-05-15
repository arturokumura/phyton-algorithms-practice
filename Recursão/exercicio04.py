'''4. Crie uma função para calcular o resto da divisão inteira.'''
def resto(num,div):
    if num   < div:
        return num
    else:
        return resto(num- div,div)
print(resto(144,12))
