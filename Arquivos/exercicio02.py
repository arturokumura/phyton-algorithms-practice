'''Escreva uma função que receba como parâmetro de entrada o nome de um arquivo
texto e retorne a quantidade de caracteres do arquivo.'''
def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

lista = [['Artur Okumura', '18', 'python'],
         ['Vagner Silva', '20', 'Java'],
         ['Abner Vinicius','21','C++']]

if len(lista):
    ref_arq = open('lista_teste.txt', 'w')
    for pessoa in lista:
        linha = pessoa[0] + '\t' + pessoa[1] + '\t' + pessoa[2] + '\n'
        ref_arq.write(linha)
    ref_arq.close()

texto = ''
if Existe_Arquivo('lista_teste.txt'):
    ref_arq = open('lista_teste.txt','r')
    texto += ref_arq.read()
ref_arq.close()
print(len(texto))
    

    
