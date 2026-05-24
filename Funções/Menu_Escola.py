def verificar_disciplina(nome_d,disciplinas):
    for i in range(len(disciplinas)):
        if disciplinas[i] == nome_d:
            return True
    return False


def cadastrar_turma(escola,disciplinas):
    nome_d = input("Disciplina: ")
    while verificar_disciplina(nome_d,disciplinas):
        print("Disciplina ja cadastrada!")
        nome_d = input("Disciplina: ")
    nome = input("Aluno: ")
    idade = int(input("Idade: "))
    notas = []
    nota = input("Nota: ")
    while nota != "":
        notas.append(float(nota))
        nota = input("Nota: ")
    aluno = [nome,idade,notas]
    turma = [aluno]
    turma.append(aluno)
    escola.append(turma)
    disciplinas.append(nome_d)
    
def cadastrar_aluno(escola, disciplinas,disciplina):
    indice = -1
    # procura a disciplina
    for i in range(len(disciplinas)):
        if disciplinas[i] == disciplina:
            indice = i
    if indice == -1:
        print("Disciplina não encontrada!")
        return
    turma = escola[indice]
    nome = input("Nome do aluno: ")
    # verifica nome repetido
    repetido  =False
    for i in range(len(turma)):
        if turma[i][0] == nome:
            repetido = True
    if repetido:
        print("Aluno já cadastrado!")
    else:
        idade = int(input("Idade: "))
        notas = []
        nota = input("Nota: ")
        while nota != "":
            notas = notas + [float(nota)]
            nota = input("Nota: ")
        novo_aluno = [nome, idade, notas]
        escola[indice] = escola[indice] + [novo_aluno]
        print("Aluno cadastrado com sucesso!")

def media(escola):
    maior = 0
    nome = ""
    for i in range(len(escola)):
        for j in range(len(escola[i])):
            soma = 0
            notas = escola[i][j][2]
            if len(notas) > 0:
                for n in notas:
                    soma += n
                media_aluno = soma / len(notas)
                if media_aluno > maior:
                    nome = escola[i][j][0]
                    maior = media_aluno
    if nome != "":
        for turma in escola:
            for aluno in turma:
                if aluno[0] == nome:
                    print(f"Nome: {aluno[0]}")
                    print(f"Idade: {aluno[1]}")
                    print(f"Notas: {aluno[2]}")
                    print("Média: {media}")
    else:
        print("Nenhum aluno encontrado!")


Escola = [ ['André Coelho', 19, [7.5, 9.2, 8.9, 6.0]], ['Rebeca Farias', 20, [9.5, 7.8]] ],
[ ['Tiago Silva', 19, [4.5, 6.1, 7.4]], ['Bárbara Andrade', 18, [5.0, 8.2, 7.6]]]
Disciplinas = ['Algoritmos e Programação', 'Segurança’']
opcao = ""
while opcao != 5:
    print("[1]- Cadastrar nova turma de alunos")
    print("[2]- Cadastrar novo aluno")
    print("[3]- Remover aluno")
    print("[4]- Mostrar dados do alunos que possuem ")
    print()
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        cadastrar_turma(Escola,Disciplinas)
    elif opcao == 2:
        disciplina = input("Disciplina: ")
        cadastrar_aluno(Escola, Disciplinas, disciplina)
    elif opcao == 4:
        media(Escola)

    
    print(f"Escola: {Escola}")
    print(f"Disciplinas: {Disciplinas}")   
    
    

