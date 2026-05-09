'''1.LISTA DE CHAMADA
Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela
prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: ela
colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um
determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada.
O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber
qual número corresponde a qual aluno. Ela sabe os nomes de todos os alunos, e que os
números deles, de 1 até N , são atribuídos de acordo com a ordem alfabética, mas os
alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor.
Tarefa
Dado os nomes dos alunos da Tia Joana e o número sorteado, determine o nome do
aluno que deve receber o bônus.
Entrada
A primeira linha contém dois inteiros N e K separados por um espaço em branco (1
≤ K ≤ N ≤ 100). Cada uma das N linhas seguintes contém uma cadeia de caracteres de
tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. Os nomes são
compostos apenas por letras minúsculas de "a" a "z".
Saída
Seu programa deve imprimir uma única linha, contendo o nome do aluno que deve
receber o bônus. '''
N = int(input("Quantos alunos? "))
K = int(input("Aluno sorteado: "))
# Lista para armazenar os nomes
nomes = []

# Lê os N nomes
for i in range(N):
    nome = input()
    nomes.append(nome)

# Ordenação em ordem alfabética (sem usar sort)
for i in range(N - 1):
    for j in range(i + 1, N):
        # Se o nome na posição i vier depois do nome na posição j,
        # troca os dois de lugar
        if nomes[i] > nomes[j]:
            aux = nomes[i]
            nomes[i] = nomes[j]
            nomes[j] = aux

# Imprime o K-ésimo nome (K começa em 1, índices começam em 0)
print(nomes[K - 1])
                
        
