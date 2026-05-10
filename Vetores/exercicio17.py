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

while opcao != 6:
    print()
    print("Agenda telefônica")
    print()
    print("[1]- Incluir contato e telefone")
    print("[2]- Alterar um telefone de um contato")
    print("[3]- Excluir um telefone de um contato")
    print("[4]- Consultar os telefones de um contato (forma formatada)")
    print("[5]- Listar todos os contatos e seus respectivos telefones (forma formatada")
    print("[6]- FIM")
    print()
    opcao = int(input("Informe uma opção: "))

    if opcao == 1:
        achou = False
        nome = input("Nome: ")

        #verificar se o nome ja existe:
        if len(agenda) != 0:
            for elemento in agenda:
                if elemento[0] == nome:
                    print("Nome ja cadastrado")
                    achou = True
        if not achou:
            contato = []
            contato.append(nome)
            

            #telefone
            tel = input("Telefone: ")
            while tel == '':
                tel = input("Telefone inválido! Digite novamente: ")
            telefones = []
            telefones.append(tel)
            while tel != '' :
                tel = input("Telefone: ")
                if tel != '':
                    telefones.append(tel)
                    
            contato.append(telefones)
            agenda.append(contato)
            print(f"Contato: {contato}")
            print(f"Agenda:{agenda}")

    if opcao == 2:
        achou = False
        nome = input("Qual contato será alterado? ")
        
        for elemento in agenda:
            if elemento[0] == nome:
                contato_mod = elemento
                achou = True
                
                #Print dos telefones
                telefones = []
                for tel in contato_mod[1]:
                    telefones.append(tel)
                    print(tel)
                
                #Alterar telefone
                encontrou_tel = False
                while not encontrou_tel:
                   alterar = input("Informe o telefone a ser alterado: ")

                # percorre todos os telefones
                   for i in range(len(contato_mod[1])):
                      if contato_mod[1][i] == alterar:
                         ind = i             
                         encontrou_tel = True

                # se terminou o for e não encontrou, pede novamente
                   if not encontrou_tel:
                       print("Telefone não encontrado!")

                
                novo = input("Informe o novo telefone: ")
                confirm = input(f"Confirmar a alteração de {contato_mod[1][i-1]} para {novo}? (s/n): ")
                if confirm.lower() == 's':
                    contato_mod[1][ind] = novo
                else:
                    print("Alteração cancelada")
                print(agenda)
                    
        if not achou:
            print("Contato não cadastrado! ")

    #Opção 3
    if opcao == 3:
        achou = False
        nome = input("Informe o contato em que deseja excluir o telefone: ")
        for elemento in agenda:
            if elemento[0] == nome:
                contato = elemento
                achou = True

                #Printar telefones
                telefones = []
                for tel in contato[1]:
                    telefones.append(tel)
                    print(tel)

                #Verificar se tem
                tem = False
                ind = 0
                while not tem:
                    excluido = input("Informe qual telefone excluir: ")
                    for i in range(len(telefones)):
                        if contato[1][i] == excluido:
                            ind  = i
                            tem = True

                    if not tem:
                        print("Telefone não encontrado!")
                        
                confirm = input(f"Confirmar a deleção do telefone {contato[1][ind]}? (s/n) ")
                if confirm.lower() == "s":
                    del contato[1][ind]
                else:
                    print("Alteração cancelada")
                print(f"Agenda: {agenda}")

        if not achou:
           print("Contato não cadastrado!")

   #Opção 4
    if opcao == 4:
        achou =  False
        nome = input("Informe o contato: ")
        for elemento in agenda:
            if elemento[0] == nome:
                contato = elemento
                achou = True
                telefones = ""
                for tel in contato[1]:
                    telefones += tel + " "
                print(f"Contato: {nome}")
                print(f"Telefones: {telefones}")

        if not achou:
            print("Contato não cadastrado")

    #Opção 5
    if opcao == 5:
        for elemento in agenda:
            print(elemento[0])
            print(elemento[1])
                
                
            
            
            
        
        
       
