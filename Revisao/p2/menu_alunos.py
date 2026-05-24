Alunos=[ ['João Pedro Souza', 18], ['Isabela Moraes', 17], ['Daniel Silva', 19] ]
Notas = [
[ ['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6] ], # provas do João
[ ['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3] ], # provas da Isabela
[ ['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1] ] # provas do Daniel
 ]
'''Faça uma função que receba por parâmetro as estruturas de dados necessárias e o nome de
um aluno. A função deve retornar uma lista contendo os nomes das disciplinas com sua
respectiva média simples parcial (dependendo do número de provas que foi realizado).
Mostre esses dados de modo formatado no programa principal;'''
def media_disciplinas(alunos, notas, nome):
    tem = False

    for i in range(len(alunos)):
        if alunos[i][0] == nome:
            indice = i
            tem = True
            media = []
            for prova in notas[indice]:
                achou = False
                for c in range(len(media)):
                    if media[c][0] == prova[0]:
                        media[c][1] += prova[2]
                        media[c][2] += 1
                        achou = True
                if not achou:
                     l = [prova[0],prova[2],1]
                     media.append(l)
            for k in range(len(media)):
                media[k][1] = media[k][1] / media[k][2]
            print( media)
    if not tem:
        print("Aluno não cadastrado!")

def maior_nota(alunos, notas, disciplina):

    maior = 0
    tem = False
    listav = []

    for i in range(len(notas)):
        for j in range(len(notas[i])):
            if notas[i][j][0] == disciplina:
                tem = True
                if notas[i][j][2] > maior:
                    maior = notas[i][j][2]
                    listav = []
                    listav.append([alunos[i][0], maior])
                elif notas[i][j][2] == maior:
                    listav.append([alunos[i][0], maior])
    if not tem:
        print("Disciplina não encontrada")
    else:
        return listav

#Programa Principal
Alunos = [
    ['João Pedro Souza', 18],
    ['Isabela Moraes', 17],
    ['Daniel Silva', 19]
]
Notas = [
    [['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6]],
    
    [['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3]],
    
    [['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1]]
]

print(maior_nota(Alunos,Notas,'MAT'))

