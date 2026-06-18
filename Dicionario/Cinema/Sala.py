Sala = {1: ('Sala 1 - VIP', '50', '3D/IMAX','Sim'), 2: ('Sala 2 - Premium', '120', '2D/IMAX', 'Não')}
def inserir_sala(sala):
    codigo = int(input("Código: "))
    if codigo in sala:
        return 1
    else:
        nome = input("Nome sala: ")
        capacidade = input("Capacidade: ")
        tipoExibicao = input("Tipo exibição: ")
        acessivel = input("Acessível: ")
        tupla = (nome,capacidade, tipoExibicao, acessivel)
        sala[codigo] = tupla
        return sala

def alterar_sala(sala):
    codigo = int(input("Código: "))
    if codigo not in sala:
        return 1
    else:
        nome = input("Nome sala: ")
        capacidade = input("Capacidade: ")
        tipoExibicao = input("Tipo exibição: ")
        acessivel = input("Acessível: ")
        tupla = (nome,capacidade, tipoExibicao, acessivel)
        confirm = input(f"Confimar alteração de dados da sala {codigo}?(s/n) ")
        if confirm == 's':
            sala[codigo] = tupla
            return sala
        else:
            return 2

def excluir_dado(sala):
    codigo = int(input("Código: "))
    if codigo in sala:
        lista = ["nome sala", "capacidade", "tipo exibição", "acessível"]
        dados = list(sala[codigo])
        print("Nome sala")
        print("Capacidade")
        print("Tipo exibição")
        print("Acessível")
        dado = input("Excluir dado: ")
        if dado.lower() not in lista:
            return 1
        else:
            if dado.lower() == lista[0]:
                dados[0] = ''
                sala[codigo] = tuple(dados)
                return sala
            elif dado.lower() == lista[1]:
                dados[1] = ''
                sala[codigo] = tuple(dados)
                return sala
            elif dado.lower() == lista[2]:
                dados[2] = ''
                sala[codigo] = tuple(dados)
                return sala
            elif dado.lower() == lista[3]:
                dados[3] = ''
                sala[codigo] = tuple(dados)
                return sala
    else:
        return 2

def exibir_dados(sala):
    print("-------------Salas----------------")
    for chave,valor in sala.items():
        print("------------------------------")
        print(f"Código: {chave}")
        print(f"Nome: {valor[0]}")
        print(f"Capacidade: {valor[1]}")
        print(f"Tipo exibição: {valor[2]}")
        print(f"Acessível: {valor[3]}")
        print()

def exibir_dado(sala):
    codigo = int(input("Código: "))
    if codigo in sala:
        print("---------------------------")
        for chave,valor in sala.items():
            if chave == codigo:
                print(f"Código: {chave}")
                print(f"Nome: {valor[0]}")
                print(f"Capacidade: {valor[1]}")
                print(f"Tipo exibição: {valor[2]}")
                print(f"Acessível: {valor[3]}")
                print()
    else:
        return 1
    
def gravar_dados(sala):
    ref_arq = open("Salas.txt", 'w')
    for chave,valor in sala.items():
        linha = str(chave) + '*' + valor[0] + '&' + valor[1] + ';' + valor[2] + ';' + valor[3] +';' + '\n'
        ref_arq.write(linha)
    ref_arq.close()
    print("Arquivo criado com sucesso!")

def ler_dados(sala):
    ref_arq = open("Salas.txt", 'r')
    for linha in ref_arq:
        linha = linha[:len(linha)-2]
        codigo,resto = linha.split('*')
        nome,resto = resto.split('&')
        capacidade,formato,acessivel = resto.split(';')
        
    print("Código:", codigo)
    print("Nome:", nome)
    print("Capacidade:", capacidade)
    print("Formato:", formato)
    print("Acessível:", acessivel)
    print()
        
    
opcao = -1
while opcao != 6:
    print("[1]- Inserir sala")
    print("[2]- Alterar dados")
    print("[3]- Excluir dado")
    print("[4]- Mostrar todos os dados")
    print("[5]- Exibir dados de uma sala")
    opcao = int(input("Opção: "))
    if opcao == 1:
        res = inserir_sala(Sala)
        if res == 1:
            print("Sala ja cadastrada!")
        else:
            print("Sala cadastrada!")
            print(res)
    if opcao == 2:
        res = alterar_sala(Sala)
        if res == 1:
            print("Sala não encontrada")
        elif res == 2:
            print("Alteração cancelada!")
        else:
            print(res)
    if opcao == 3:
        res = excluir_dado(Sala)
        if res == 1:
            print("Dado não encontrado!")
        elif res == 2:
            print("Sala não encontrada!")
        else:
            print(res)
    if opcao == 4:
        exibir_dados(Sala)
    if opcao == 5:
        res = exibir_dado(Sala)
        if res == 1:
            print("Sala não encontrada")
        else:
            exibir_dado(Sala)
    gravar_dados(Sala)
    if opcao == 6:
        ler_dados(Sala)
