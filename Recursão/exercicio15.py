'''Faça uma função recursiva para eliminar apenas a primeira ocorrência de uma
determinada letra de uma string'''
def remover(frase,letra,flag = False):
    if len(frase) == 0:
        return ""
    else:
        if frase[0] == letra and not flag:
            return remover(frase[1:],l,True)
        
        else:
            return frase[0] + remover(frase[1:],l,flag)

            
s = "abacaxi aa"
l = "a"
print(remover(s,l))
                                        
