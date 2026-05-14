'''Crie uma função para calcular a potência xy.'''
def pot(x,y):
    if y == 0:
        return 1
    else:
        return x * pot(x, y -1)
    
a,b = 2,3
print(pot(a,b))
