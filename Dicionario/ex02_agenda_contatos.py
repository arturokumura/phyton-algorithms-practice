'''2. Reescreva o sistema de cadastro de alunos utilizando como
estruturas de dados dicionários e tuplas ao invés de listas.
dic_alunos[(RA, nome)] = (data_nasc,[e-mails],[telefones])'''
dic_alunos = {}

def adicionar_contato(dic_alunos, ra, nome, data_nascimento, lista_emails, lista_telefones):
    for chave in dic_alunos:
        if chave[0] == ra:
            print("Aluno já cadastrado!")
            return
    dic_alunos[(ra, nome)] = (data_nascimento, lista_emails, lista_telefones)

def exibir_contato(dic_alunos, ra):
    for (ra_aluno, nome), (data, emails, telefones) in dic_alunos.items():
        if ra_aluno == ra:
            print("RA:", ra_aluno)
            print("Nome:", nome)
            print("Data de nascimento:", data)
            print("Emails:")
            for email in emails:
                print("-", email)

            print("Telefones:")
            for telefone in telefones:
                print("-", telefone)
            return

    print("Contato não cadastrado!")

def excluir_contato(dic_alunos, ra, nome):
    if (ra, nome) in dic_alunos:
        del dic_alunos[(ra, nome)]
        print("Contato excluído!")
    else:
        print("Contato não encontrado!")

def alterar_contato(dic_alunos, ra):
    for chave in dic_alunos:
        if chave[0] == ra:
            nome = input("Novo nome: ")
            data = input("Nova data de nascimento: ")
            emails = []
            email = input("Email (ENTER para parar): ")
            while email != "":
                emails.append(email)
                email = input("Email (ENTER para parar): ")

            telefones = []
            telefone = input("Telefone (ENTER para parar): ")
            while telefone != "":
                telefones.append(telefone)
                telefone = input("Telefone (ENTER para parar): ")

            del dic_alunos[chave]
            dic_alunos[(ra, nome)] = (data, emails, telefones)

            print("Contato alterado!")
            return

    print("Contato não cadastrado!")
opcao = ''

while opcao != 5:
    print("[1].Adicionar Contato")
    print("[2].Exibir Contato")
    print("[3].Excluir Contato")
    print("[4].Alterar Contato")
    print("[5]-Sair")
    opcao = int(input("Opção: "))
    print(dic_alunos)
    if opcao == 1:
        l_email = []
        l_tel= []
        RA = input("Ra:: ")
        name = input("Nome: ")
        data_nascim = input("Data de nascimento: ")
        email= input("Email: ")
        while email != "":
            l_email.append(email)
            email = input("Email: ")
        teles= input("Telefones: ")
        while teles != "":
            l_tel.append(teles)
            teles = input("Telefone: ")
        adicionar_contato(dic_alunos,RA,name,data_nascim,l_email,l_tel)
    if opcao == 2:
        RA = input("RA: ")
        exibir_contato(dic_alunos, RA)
    if opcao == 3:
        RA = input("Ra: ")
        name = input("Nome: ")
        confirm = input("Confirmar exclusão?(s/n) ")
        if confirm == 's':
            excluir_contato(dic_alunos,RA,name)
        else:
            print("Alteração cancelada!")
    if opcao == 4:
        RA = input("Ra: ")
        alterar_dados(dic_alunos,RA)
