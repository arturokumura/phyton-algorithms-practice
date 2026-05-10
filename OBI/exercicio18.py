'''4.Times
As aulas de educação física, em muitas escolas, acontecem da seguinte maneira: O
professor entrega uma bola ao alunos (geralmente de futebol) e estes se dividem em
times, onde jogam partidas alternadamente.
A maneira como os times são escolhidos também é semelhante em todas as escolas:
decide-se quantos times serão formados, e uma pessoa para montar cada um dos times.
Cada pessoa vai escolher, alternadamente, um dos alunos restantes para fazer parte de
sua equipe. Como todos querem ter uma boa equipe, a pessoa que vai escolher o
próximo membro do time escolhe aquele, dentre os ainda disponíveis, que possui o
melhor nível de habilidade. Assim, os times acabam ficando relativamente equilibrados
na soma do nível de habilidade dos jogadores.
Tarefa
Dada uma lista de alunos que serão escolhidos e seus respectivos níveis de habilidade
para os times e a quantidade de times que serão formados, mostre como ficarão os
times ao final do processo de montagem dos mesmos.
Entrada
A primeira linha da entrada contém dois inteiros N (2 ≤ N ≤ 10.000) e T (2 ≤ T ≤ 1000),
representando respectivamente a quantidade de alunos e o número de times a serem
formados, sendo T ≤ N. As N linhas seguintes descrevem, cada uma, um aluno
disponível para escolha de times. Cada uma dessas linhas possui o nome do aluno
(composto apenas por letras minúsculas) e um inteiro H (0 ≤ H ≤ 1.000.000)
descrevendo seu nível de habilidade).
Não existem dois alunos com o mesmo nível de habilidade, e todos eles possuem
nomes diferentes. É possível que alguns times acabem ficando com menos jogadores do
que os outros.
Saída
Seu programa deve imprimir a lista de times que será formada ao final do processo de
seleção. Para cada time, você deverá mostrar o termo "Time N", onde N é o número do
time (1 para o primeiro, 2 para o segundo, e assim por diante) seguido de K linhas,
onde K é a quantidade de jogadores do time, mostrando o nome de cada um dos
jogadores do time, em ordem alfabética. Imprima uma linha em branco após cada
descrição de time (inclusive do último).
Os times serão escolhidos pelo computador, então não é necessário considerar o aluno
que irá fazer a escolha dos times.'''

N = int(input("Quantidade de alunos: "))
T = int(input("Número de times: "))
alunos = []

for i in range(N):
    aluno = input("Aluno: ")
    h = int(input("Habilidade: "))
    alunos.append([aluno, h])

# -------------------------------------------------
# Ordena os alunos pela habilidade (maior para menor)
# -------------------------------------------------
for i in range(N - 1):
    for j in range(i + 1, N):
        if alunos[i][1] < alunos[j][1]:
            aux = alunos[i]
            alunos[i] = alunos[j]
            alunos[j] = aux

# -------------------------------------------------
# Cria os times vazios
# -------------------------------------------------
times = []

for i in range(T):
    times.append([])

# -------------------------------------------------
# Distribui os alunos nos times
# aluno 0 -> time 1
# aluno 1 -> time 2
# ...
# -------------------------------------------------
for i in range(N):
    indice_time = i % T
    times[indice_time].append(alunos[i][0])   # guarda apenas o nome

# -------------------------------------------------
# Ordena alfabeticamente os nomes de cada time
# -------------------------------------------------
for i in range(T):
    for j in range(len(times[i]) - 1):
        for k in range(j + 1, len(times[i])):
            if times[i][j] > times[i][k]:
                aux = times[i][j]
                times[i][j] = times[i][k]
                times[i][k] = aux

# -------------------------------------------------
# Imprime os times
# -------------------------------------------------
for i in range(T):
    print("Time", i + 1)

    for nome in times[i]:
        print(nome)

    print()
