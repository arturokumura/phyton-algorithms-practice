'''Faça uma função recursiva para eliminar todas as ocorrências de uma
determinada letra de uma string'''
def remover_Letra(s,l):
    if len(s) == 0:
        return ""
    else:
        if s[0] == l:
            return remover_Letra(s[1:],l)
        else:
            return s[0] + remover_Letra(s[1:],l)

frase = "abacaxi aa"
letra = "a"
print(remover_Letra(frase,letra))
