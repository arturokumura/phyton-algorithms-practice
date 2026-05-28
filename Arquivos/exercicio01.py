'''Escreva uma função que receba como parâmetro de entrada o nome de um arquivo
texto e retorne a quantidade de linhas do arquivo.'''
def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
cont = 0
if Existe_Arquivo("cad_alunos.txt"):
    ref_arq = open("cad_alunos.txt", 'r')
    for linha in ref_arq:
        cont += 1
    ref_arq.close()
print(f"Total de linhas: {cont}")
    
    
