'''Faça um programa em Python que inicie com as duas estruturas de dados vazias e fique em execução até
o usuário escolher a opção “Finalizar o programa” do seguinte menu:
1. Cadastrar um novo aluno sem repetição de nome
2. Consultar a idade de um aluno a partir de seu nome
3. Alterar a idade de um aluno a partir de seu nome
4. Remover um aluno a partir de seu nome
5. Cadastrar a nota de uma prova de uma disciplina para um aluno a partir de seu nome
6. Consultar todas as notas de provas de todas as disciplinas de um aluno a partir de seu nome
7. Alterar a nota de uma prova de uma disciplina para um aluno a partir de seu nome/disciplina/prova
8. Remover uma prova de uma disciplina com sua respectiva nota de um aluno a partir de seu
nome/disciplina/prova
9. Finalizar o programa'''

alunos = []
notas = []
opcao = 0
while opcao != 9:
    print("----------Menu----------")
    print()
    print("[1]-Cadastrar novo aluno")
    print("[2]-Consultar a idade de um aluno")
    print("[3]-Alterar a idade de um aluno")
    print("[4]-Remover um aluno")
    print("[5]-Cadastrar a nota de uma prova")
    print("[6]-Consultar todas as notas de provas")
    print("[7]-Alterar a nota de uma prova de uma disciplina")
    print("[8]-Remover uma prova de uma disciplina")
    print("[9]-Finalizar programa")
    print()
    opcao = int(input("Escolha uma opção: "))

    #Opção 1
    if opcao == 1:
        achou = False
        nome = input("Informe um nome: ")
        
        for elemento in alunos:
            if elemento[0] == nome:
                print("Aluno ja cadastrado!")
                achou = True
            
        if not achou:
            idade = int(input("Informe a idade do aluno: "))
            dados = []
            dados.append(nome)
            dados.append(idade)
            alunos.append(dados)
            print("Aluno cadastrado!")
    #Opção2
    if opcao == 2:
        nome = input("Consultar idade do aluno: ")
        achou_nome = False
        for elemento in alunos:
            if elemento[0] == nome:
                idade = elemento[1]
                print(idade)
                achou_nome = True
        if not achou_nome:
            print("Aluno não cadastrado")

    #Opcao3
    if opcao == 3:
        print(alunos)
        nome = input("Alterar a idade do aluno: ")
        achou = False
        for elemento in alunos:
            if elemento[0] == nome:
                idade = elemento[1]
                alterar = int(input("Alterar para qual idade? "))
                confirmar = input("Confimar alteração?(s/n) ")
                if confirmar.lower() == 's':
                    print("Alteração realizada com sucesso")
                    elemento[1] = alterar
                    achou = True
                else:
                    print("ALteração cancelada")
                    achou = True

        if not achou:
            print("Aluno não cadastrado")

    #Opcao 4
    if opcao == 4:
        achou = False
        nome = input("Remover aluno: ")
        
        for i in range(len(alunos)):
            if alunos[i][0] == nome and not achou:
                ind = i
                confirmar = input("Confirmar exclusão(s/n): ")
                if confirmar.lower() == 's':
                    del alunos[ind]
                    print("Exclusão realizada com sucesso!")
                    achou = True
                else:
                    print("Exclusão cancelada")
                    achou = True

        if not achou:
            print("Aluno não cadastrado")

    #Opcao 5
    if opcao == 5:
        achou = False
        achou_d = False
        nome = input("Nome do aluno: ")

        for i in range(len(alunos)):
            if alunos[i][0] == nome:
                achou =  True
                disciplina = input("Código da disciplina: ")
                prova = input("Nome da prova (ex: P1, P2, P3): ")
                nota = float(input("Nota: "))

            
                notas_aluno = []
                notas_aluno.append(disciplina.upper())
                notas_aluno.append(prova.upper())
                notas_aluno.append(nota)

                #Macete
                while len(notas) <= i:
                   notas.append([])

                notas[i].append(notas_aluno)
                print("Nota cadastrada com sucesso!")

        if not achou:
                print("Aluno não encontrado!")
    

    #Opcao 6
    if opcao == 6:
        achou = False
        ind = 0
        nome = input("Consultar notas do aluno: ")
        for i in range(len(alunos)):
            if alunos[i][0] == nome:
                 achou =  True
                 ind  = i

            
                 for j in range(len(notas[ind])):
                    print("| Nota:", notas[ind][j][2])
        if not achou:
            print("Aluno não cadastrado!")

    #Opcao 7
    if opcao == 7:
        achou = False
        achou_nota = False

        nome = input("Nome do aluno: ")

        # Procura o aluno
        for i in range(len(alunos)):
            if alunos[i][0] == nome:
                achou = True
                ind = i

        if achou:
            disciplina = input("Código da disciplina: ")
            prova = input("Nome da prova: ")

            # Procura a disciplina e a prova
            for j in range(len(notas[ind])):
                if notas[ind][j][0] == disciplina.upper() and notas[ind][j][1] == prova.upper():
                    nova_nota = float(input("Nova nota: "))
                    notas[ind][j][2] = nova_nota
                    print("Nota alterada com sucesso!")
                    achou_nota = True

            if not achou_nota:
                print("Disciplina/prova não encontrada.")
        else:
            print("Aluno não encontrado.")
   
    #Opcao 8
    ind = 0
    if opcao == 8:
        achou = False
        achou_nota = False

        nome = input("Nome do aluno: ")

        for i in range(len(alunos)):
            if alunos[i][0] == nome:
                achou = True
                ind = i
        if achou:
            disciplina = input("Código da disciplina: ")
            prova = input("Nome da prova: ")

            indice_remover = -1
            for j in range(len(notas[ind])):
                if notas[ind][j][0] == disciplina.upper() or notas[ind][j][1] == prova.upper() and not achou_nota:
                     indice_remover = j
                     achou_nota = True
            if indice_remover != -1:
                del notas[ind][indice_remover]
                print("Prova removida com sucesso!")
            if not achou:
                print("Disciplina/prova não encontrada")
        else:
            print("Aluno não encontrado")
    print(alunos)
    print(notas)
                      
