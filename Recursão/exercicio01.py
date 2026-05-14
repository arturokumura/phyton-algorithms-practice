'''Crie uma função para calcular o fatorial de um número.'''
def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n -1)

num  = 5
print(fat(num))
    
