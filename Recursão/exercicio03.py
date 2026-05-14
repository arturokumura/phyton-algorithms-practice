'''Crie uma função para calcular o quociente da divisão inteira.'''
def div(d1,d2):
    if d1 < d2:
        return 0
    else:
        return 1 + div(d1 - d2, d2)

n, d = 10 ,3
print(div(n,d))
