Locais= {
("Nirvana", "MorumBis", "20/12/2024") : [250.00, 130000 ],
("Beatles", "Allianz Parque", "15/01/2025"): [850.00, 50000],
("Queen","Neo Química Arena", "05/02/2025"): [1000.00, 20000]
}
def inserir_show(locais):
    banda = input("Banda: ")
    local = input("Local: ")
    data = input("Data(xx/yy/zzzz): ")
    valor_ingresso = float(input("Valor ingresso: "))
    tupla = (banda,local,data)
    if tupla in locais:
        return "Show ja cadastrado"
    else:
        for chave,valor in locais.items():
            if local in chave:
                nome = chave
                ingressos = float(input("Ingressos: "))
                if locais[nome][1] > ingressos:
                    locais[tupla] = [valor_ingresso,ingressos]
                    return "Show cadastrado com sucesso"
                else:
                    return "Capacidade não comporta total de ingressos"
        else:
            return "Local não encontrado!"

def alterar_dados(locais,chave):
    if chave in locais:
        banda = chave[0]
        local = input("Novo local: ")
        data = input("Nova data: ")
        valor_ingresso = float(input("Novo valor ingersso: "))
        capacidade = float(input("Nova capacidade: "))
        locais.pop(chave)
        tupla = (banda,local,data)
        locais[tupla] = [valor_ingresso,capacidade]
        return locais
    else:
        return "Local não encontrado!"

def exibir_shows(locais,local):
    lista = []
    cont  = 0
    for chave,valor in locais.items():
        if chave[1] == local:
            cont += 1
            dados = [chave[0], chave[2]]
            lista.append(dados)
    if cont == 0:
        return "Nenhum show"
    else:
        return lista

def exibir_dados(locais):
    lista = []
    for chave in locais.keys():
        lista.append(chave)
    for i in range(len(lista)):
        menor = i
        x = lista[i]
        for j in range(i + 1,len(lista)):
            if lista[j] < x:
                lista[menor] = lista[j]
                lista[j] = x
    return lista

def maior_preco(locais):
    maior = 0    
    lista =[]
    for chave,valor in locais.items():
        if valor[0] > maior:
            maior = valor[0]
            lista = [chave]
        elif valor[0] == maior:
            lista.append(chave)
    return lista

def gravar_arquivo(locais):
    ref_arq = open("Shows.txt", 'w')
    for chave,valor in locais.items():
        linha = chave[0] +';'+ chave[1] + ';'+ chave[2] +';'+ str(valor[0]) +';'+str(valor[1]) + '\n'
        ref_arq.write(linha)
    ref_arq.close()
    return "Arquivo gravado com sucesso!"
        
opcao =0
while opcao != 8:
    print("[1]- Inserir show")
    print("[2]- Alterar dados")
    print("[3]- Exibir shows")
    print("[4]- Exibir dados de shows")
    print("[5]- Maior preço de ingresso")
    print(gravar_arquivo(Locais))
    print(Locais)
    
    opcao = int(input("Opção: "))
    

    if opcao == 1:
        print(inserir_show(Locais))
    if opcao == 2:
        banda  =input("Banda: ")
        local = input("Local: ")
        data  = input("Data: ")
        dados = (banda,local,data)
        print(alterar_dados(Locais,dados))
    if opcao == 3:
        Local = input("Local: ")
        res = exibir_shows(Locais,Local)
        for i in range(len(res)):
            print(f"Banda: {res[i][0]}")
            print(f"Data: {res[i][1]}")
    if opcao == 4:
        res = exibir_dados(Locais)
        for i in range(len(res)):
            print("--------------")
            print(f"Banda: {res[i][0]}")
            print(f"Local: {res[i][1]}")
            print(f"Data: {res[i][2]}")
    if opcao == 5:
        res = maior_preco(Locais)
        print(res)
        for i in range(len(res)):
            print("--------------")
            print(f"Banda: {res[i][0]}")
            print(f"Local: {res[i][1]}")
            print(f"Data: {res[i][2]}")
            
