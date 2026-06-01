'''Implemente um sistema de gerenciamento de contatos de
prestadores de serviços, cuja chave deve ser o e-mail
pessoal. As informações adicionais do contato devem estar
em uma lista: nome, data de nascimento e uma lista de
tuplas, onde cada tupla deve conter a especialidade
(encanador, mecânico etc) e valor da hora. O menu do
sistema deve oferecer as seguintes opções:'''

contatos = {}
def adicionar_contato(email,nome,data_nasc, espec, valorh):
    tupla = (espec,valorh)
    contatos[email] = [[nome,data_nasc,[tupla]]]
    print(contatos)

def exibir_contato(email):
    print(contatos.get(email,"Contato não encontrado"))

def excluir_contato(email):
    del contatos[email]

def alterar_dados(contatos):
    email = input("Digite o e-mail do contato: ")

    if email in contatos:
        print("Dados atuais:", contatos[email])

        nome = input("Novo nome: ")
        nascimento = input("Nova data de nascimento: ")

        contatos[email][0] = nome
        contatos[email][1] = nascimento

        print("Dados alterados com sucesso!")
    else:
        print("Contato não encontrado.")    

opcao = ''
while opcao != 5:
    print("[1].Adicionar Contato")
    print("[2].Exibir Contato")
    print("[3].Excluir Contato")
    print("[4].Alterar Contato")
    print("[5]-Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        mail = input("Email: ")
        name = input("Nome: ")
        data_nascim = input("Data de nascimento: ")
        especialidade = input("Especialidade: ")
        valor_h = int(input("Valor por hora; "))
        adicionar_contato(mail,name,data_nascim,especialidade,valor_h)
    if opcao == 2:
        mail = input("Email: ")
        exibir_contato(mail)
    if opcao == 3:
        mail = input("Email: ")
        confirm = input("Confirmar exclusão?(s/n) ")
        if confirm == 's':
            excluir_contato(mail)
        else:
            print("Alteração cancelada!")
    if opcao == 4:
        alterar_dados(contatos)


