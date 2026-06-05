'''
e) consultarTelefone – essa função retorna os telefones de uma pessoa na
agenda. '''
Agenda = {}
        
def incluirNovoNome(agenda,nome,telefones):
    achou = False
    for chave in agenda:
        if chave == nome:
            achou = True
    if achou:
        print("Nome ja está na agenda!")
    else:
        agenda[nome] = telefones

def incluirTelefone(agenda, nome, telefone_novo):
    if nome in agenda:
        agenda[nome].append(telefone_novo)
        print("Telefone incluído com sucesso!")
    else:
        print("Contato não encontrado!")
        confirm = input("Adicionar contato? (s/n) ")
        if confirm.lower() == 's':
            telefones = [telefone_novo]
            tel = input("Outro telefone (ENTER para finalizar): ")
            while tel != "":
                telefones.append(tel)
                tel = input("Outro telefone (ENTER para finalizar): ")

            incluirNovoNome(agenda, nome, telefones)
            print("Contato adicionado!")
        else:
            print("Alteração cancelada!")

def excluirTelefone(agenda,nome,tel_exc):
    if nome in agenda:
        telefones = agenda[nome]
        if len(telefones) == 1:
            if telefones[0] == tel_exc:
                del agenda[nome]
        else:
            achou = False
            for i in range(len(telefones)):
                if telefones[i] == tel_exc:
                    achou = True
                    ind = i
            if not achou:
                print("Telefone não encontrado!")
            else:
                del agenda[nome][ind]
    else:
        print("Nome não encontrado!")
            
def excluirNome(agenda,nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print("Nome não encontrado!")

def consultarTelefone(agenda,nome):
    if nome in agenda:
        print(agenda[nome])
    else:
        print("Nome não encontrado!")
opcao = 0
while opcao != 6:
    print(Agenda)
    opcao = int(input("Opção: "))
    if opcao == 1:
        Nome = input("Nome: ")
        Telefones = []
        tel = input("Telefone: ")
        while tel != '':
            Telefones.append(tel)
            tel = input("Telefones: ")
        incluirNovoNome(Agenda,Nome,Telefones)
    if opcao == 2:
        Nome = input("Nome: ")
        tel_novo = input("Telefone: ")
        incluirTelefone(Agenda,Nome,tel_novo)
    if opcao == 3:
        Nome = input("Nome: ")
        Tel_exc = input("Telefone: ")
        excluirTelefone(Agenda,Nome,Tel_exc)
    if opcao == 4:
        Nome = input("Nome: ")
        excluirNome(Agenda,Nome)
    if opcao == 5:
        Nome = input("Nome: ")
        consultarTelefone(Agenda,Nome)
print(Agenda)
            
