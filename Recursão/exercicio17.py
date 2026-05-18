'''Faça uma função recursiva que retorne True se uma string é palíndromo ou
False caso contrário.'''
def palindromo(s):
    
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindromo(s[1:-1])
        
    
frase = "carro"
print(palindromo(frase))
