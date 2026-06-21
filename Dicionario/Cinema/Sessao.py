Sessao = [["Guardiões da Galaxia", 2018, 1, '20/06/2026', '19:30', 12.90],
['Bad Boys 1', 2008, 2, '04/10/2026', '21:30', 9.90]]
Teste = []
def inserir_sessao(sessao):
    nome = input("Nome: ")
    ano = int(input("Ano lançamento: "))
    cod_sala = int(input("Código sala: "))
    data = input("Data(xx/yy/zzzz): ")
    horario = input("Horário(xx:yy): ")
    
    for i in range(len(sessao)):
        if nome == sessao[i][0]:
            return -1
    
    preco = float(input("Preço ingresso: ")) 
    lista = [nome,ano,cod_sala,data,horario,preco]
    sessao.append(lista)
    return sessao

def alterar_sessao(sessoes):
    nome = input("Nome do filme: ")

    for sessao in sessoes:
        if sessao[0] == nome:
            sessao[5] = float(input("Novo preço: "))
            return 1
    return -1

def excluir_sessao(sessao):
    nome = input("Nome do filme: ")
    for i in range(len(sessao)):
        if sessao[i][0] == nome:
            del sessao[i]
            return sessao
    return -1

def exibir_sessao(sessao):
    teste= 0
    nome = input("Nome do filme: ")
    for i in range(len(sessao)):
        if sessao[i][0] == nome:
            print(f"Filme: {sessao[i][0]}")
            print(f"Ano lançamento: {sessao[i][1]}")
            print(f"Código sala: {sessao[i][2]}")
            print(f"Data: {sessao[i][3]}")
            print(f"Horário: {sessao[i][4]}")
            print(f"Preço ingresso: {sessao[i][5]}")
            teste = 1
    if teste == 0:
        print("Sessão não encontrada!")

def exibir_sessoes(sessao):
    for i in range(len(sessao)):
        print("-----------------------------")
        print(f"Filme: {sessao[i][0]}")
        print(f"Ano lançamento: {sessao[i][1]}")
        print(f"Código sala: {sessao[i][2]}")
        print(f"Data: {sessao[i][3]}")
        print(f"Horário: {sessao[i][4]}")
        print(f"Preço ingresso: {sessao[i][5]}")
        print()

def gravar_arquivo(sessao):
    ref_arq = open("Sessão.txt", 'w')
    for i in range(len(sessao)):
        linha = sessao[i][0]+'#'+str(sessao[i][1])+'$'+str(sessao[i][2])+'%'+sessao[i][3]+'*'+sessao[i][4]+'@'+str(sessao[i][5])+ '\n'
        ref_arq.write(linha)
    ref_arq.close()

def ler_arquivo(teste):
    ref_arq = open('Sessão.txt', 'r')
    for linha in ref_arq:
        linha = linha[:len(linha)-1]
        
        filme,resto = linha.split('#')
        ano,resto = resto.split('$')
        cod,resto = resto.split('%')
        data,resto = resto.split('*')
        horario,resto = resto.split('@')
        preco = resto
        lista = [filme,int(ano),int(cod),data,horario,float(preco)]
        teste.append(lista)
    ref_arq.close()
    print(f"Lista teste: {teste}")
        
        
opcao = -1
while opcao != 7:
    print("[1]- Inserir sessão")
    print("[2]- Alterar dados")
    print("[3]- Excluir sessão")
    print("[4]- Exibir sessão")
    print("[5]- Exibir sessões")
    print("[6]- Ler Arquivo")
    opcao = int(input("Opção: "))
    if opcao == 1:
        res = inserir_sessao(Sessao)
        if res == -1:
            print("Filme já cadastrado!")
        else:
            print(res)
    elif opcao ==2:
        res = alterar_sessao(Sessao)
        if res == 1:
            print("Sessão alterada com sucesso!")
        else:
            print("Sessão não encontrada!")
    elif opcao == 3:
        res = excluir_sessao(Sessao)
        if res == -1:
            print("Sessão não encontrada!")
        else:
            print(res)
    elif opcao == 4:
        exibir_sessao(Sessao)
    elif opcao == 5:
        exibir_sessoes(Sessao)
    elif opcao == 6:
        ler_arquivo(Teste)
    gravar_arquivo(Sessao)
    
