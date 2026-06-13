import os
Locais= {
"MorumBis":[ 'Praça Roberto Gomes Pedrosa', 1, 'São Paulo', 'SP', 6000000, 145000],
"Allianz Parque" : ['Avenida Francisco Matarazzo', 1705, 'São Paulo', 'SP', 1800000, 41400],
"Neo Química Arena" : [ 'Av. Miguel Ignácio Curi', 111, 'São Paulo',' SP',  2500000, 63267 ] ,
" Maracanã-Jornalista Mário Filho" : ['Rua Professor Eurico Rabelo' , 0 ,' Rio de Janeiro','RJ',8000000, 199800]
}
def existir_arquivo(nome):
    if os.path.exists(nome):
        return True
    else:
        return False

def inserir_local(locais, novo_local):
    if novo_local in locais:
        print("Nome do local já existe")
    else:
        logradouro = input("Logradouro: ")
        numero = int(input("Número: "))
        cidade= input("Cidade: ")
        estado = input("Estado: ")
        valor_aluguel = float(input("Valor do aluguel: "))
        capacidade_publico = int(input("Capacidade do público: "))
        dados = [logradouro,numero,cidade,estado,valor_aluguel,capacidade_publico]
    locais[novo_local] = dados

def alterar_dados(locais,nome):
    if nome in locais:
        logradouro = input("Logradouro: ")
        numero = int(input("Número: "))
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        valor_aluguel = float(input("Valor do aluguel: "))
        capacidade_publico = int(input("Capacidade do público: "))
        dados = [logradouro,numero,cidade,estado,valor_aluguel,capacidade_publico]
        for chave,valor in locais.items():
            if chave == nome:
                locais[chave] = dados
    else:
        print("Nome não encontrado!")

def excluir_local(locais,nome):
    if nome in locais:
        confirm = input("Confirmar alteração?(s/n): ")
        if confirm.lower() == 's':
            locais.pop(nome)
        else:
            print("Alteração cancelada!")
    else:
        print("Local não encontrado")

def exibir_dados(locais,nome):
    if nome in locais:
        c = locais[nome]
        dic = {}
        dic["Logradouro"] = c[0]
        dic["Numero"] = c[1]
        dic["Cidade"]= c[2]
        dic["Estado"] = c[3]
        dic["Valor aluguel"] = c[4]
        dic["Capacidade de público"] = c[5]
        return dic
    else:
        return "Nome não encontrado!"

def capacidade(locais,cap):
    l = []
    for chave,valor in locais.items():
        lista = []
        if valor[5] >= cap:
            lista= [chave,valor]
            l.append(lista)
    return l

def ler_dados(arq,locais):
    arq = open('Locais', 'w')
    for chave,valor in locais.items():
        local,logradouro,numero,cidade,estado,aluguel,capacidade = chave,valor[0],str(valor[1]),valor[2],valor[3],str(valor[4]),str(valor[5])
        linha = local + ';' + logradouro + ';' + numero + ';' + cidade + ';' + estado + ';' + aluguel + ';' + capacidade + '\n'
        arq.write(linha)
    arq.close()
    return "Arquivo gravado com sucesso!"        
        

opcao = 0
while opcao != 5 :
    print("[1] Inserir local")
    print("[2] Alterar local")
    print("[3] Excluir local")
    print("[4] Exibir local")
    print("[5] Exibir todos")
    print("[6] Buscar por capacidade")
    print("[7] Salvar arquivo")
    print("[0] Sair")
    print(Locais)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        Novo_local = input("Novo local: ")
        inserir_local(Locais,Novo_local)
    if opcao == 2:
        Nome = input("Local: ")
        alterar_dados(Locais,Nome)
    if opcao == 3:
        Nome = input("Local: ")
        excluir_local(Locais,Nome)
    if opcao == 4:
        Nome = input("Local: ")
        dicionario = exibir_dados(Locais,Nome)
        for chave,valor in dicionario.items():
            print(chave,':',valor)
    if opcao == 5:
        for nome in Locais:
            print(f"Local: {nome}")
            dados = exibir_dados(Locais, nome)

            for campo, valor in dados.items():
                print(f"{campo}: {valor}")
    if opcao == 6:
        Cap = int(input("Público: "))
        resultado = capacidade(Locais,Cap)
        for i in range(len(resultado)):
            print(resultado[i])
    if opcao == 7:
        print(ler_dados('Locais.txt',Locais))
        
