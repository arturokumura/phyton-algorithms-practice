def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

lista = [['SC180100','Aluno 1', 'aluno1@ifsp.edu.br'],
         ['SC180200','Aluno 2', 'aluno2@ifsp.edu.br'],
         ['SC180300','Aluno 3', 'aluno3@ifsp.edu.br']]

#gravando arquivo
if len(lista):
    ref_arq =open("cad_alunos.txt", 'w')
    for aluno in lista:
        RA, nome, email = aluno[0], aluno[1], aluno[2]
        linha = RA + "\t" + nome + "\t" + email + "\n"
        ref_arq.write(linha)
    ref_arq.close()
    print("Arquivo gravado com sucesso!")

#recuperando dados do arquivo se o arquivo existir
lista = []
if Existe_Arquivo("cad_alunos.txt"):
    ref_arq=open("cad_alunos.txt", 'r')
    for linha in ref_arq:
        linha = linha[:len(linha)-1] #removendo o '\n'
        aluno = linha.split("\t") #quebra no tab
        lista.append(aluno)
    ref_arq.close()
print(lista)

#recuperando dados do arquivo com while
print("------------Recuperando com While------------")
lista2 = []
if Existe_Arquivo("cad_alunos.txt"):
    ref_arq = open("cad_alunos.txt",'r')
    linha =  ref_arq.readline()
    while linha != '':
        linha =linha[:len(linha)-1]
        aluno = linha.split("\t")
        lista2.append(aluno)
        linha = ref_arq.readline()
    ref_arq.close()
print(lista2)

