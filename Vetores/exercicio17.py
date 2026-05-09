'''17. Usando uma lista como armazenamento conforme especificação abaixo, exiba um menu de opções
que fique em execução continuamente, até que o usuário escolha a opção de finalização. Não deve ser
permitida a inclusão de nome de contato repetido. Cada contato pode ter quantos telefones desejar.
Estrutura de dados:
Agenda=['Contato 1', ['99876-5645','98798-3244'], 'Contato 2',['99786-5531'], ..., 'Contato N',['99654-
1123', '99874-5532 ', '99874-8879’ ]]
1- Incluir contato e telefone (pelo menos um telefone)
2- Alterar um telefone de um contato (mostre as opções e o usuário digita qual será alterado)
3- Excluir um telefone de um contato (mostre as opções e o usuário digita qual será excluído
4- Consultar os telefones de um contato (forma formatada)
5- Listar todos os contatos e seus respectivos telefones (forma formatada)
6 – FIM
Digite a opção desejada: '''

opcao  = 0
agenda = []
nome = []
telefones = []
contato = []
while opcao != 6:
    print("[1]- Incluir contato e telefone (pelo menos um telefone)")
    print("[2]- Alterar um telefone de um contato (mostre as opções e o usuário digita qual será alterado")
    print("[3]- Excluir um telefone de um contato (mostre as opções e o usuário digita qual será excluído")
    print("[4]- Consultar os telefones de um contato (forma formatada")
    print("[5]- Listar todos os contatos e seus respectivos telefones (forma formatada")
    print("[6]- FIM")
    opcao = int(input("Informe uma opção: "))

    #Opção 1
    if opcao == 1:
        achou=False
           
        #inclui novo contato sem repetição
        nome=input('Nome do Contato: ')
     
        #verifica se o nome já está na agenda
        if len(agenda) != 0:
            for elemento in agenda:
                if elemento[0] == nome:
                    achou=True
                        
                        
        #se o nome NÃO estiver na agenda
        if not achou:
            contato=[]
            contato.append(nome)

            tel=input('Telefone: ')
            while tel == '':
                tel=input('O contato precisa ter pelo menos um telefone!Digite novamente!\nTelefone: ')
            telefones=[]
            telefones.append(tel)
            while tel != '':
                tel=input('Telefone: ')
                if tel != '':
                    telefones.append(tel)
            contato.append(telefones)
            print(f'Contato : {contato}')
            agenda.append(contato)
        else:
            print('Contato já cadastrado!')
                
        #para conferir
        print(f'Agenda: {agenda}')


   
        
