Bandas= {
 "Beatles" : [ 1960 ,[[ ("John Lennon", ["Guitarra", "Vocal"] ), ("Paul McCartney", ["Baixo", "Vocal"] ),("George Harrison", ["Guitarra"] ), ("Ringo Starr", ["Bateria"] ) ] ]] ,
 "Queen" : [ 1970 ,[[ ("Freddie Mercury", ["Vocal"] ), ("Brian May", ["Guitarra"] ),("Roger Taylor", ["Bateria"] ), ("John Deacon", ["Baixo"] ) ] ]] ,
 "Nirvana" : [ 1987 ,[[ ("Kurt Cobain ", ["Guitarra", "Vocal"] ), ("Krist Novoselic ", ["Baixo"] ),("Dave Grohl ", ["Bateria"] ) ]] ]
}

def inserir_banda(dic):
    nome = input("Nome da banda: ")
    if nome in dic:
        print("Esta banda já existe. Tente novamente!")
    else:
        ano = int(input("Ano: "))
        lista_integrantes =[]
        
        n = int(input("Número de integrantes: "))
        for i in range(n):
            lista_instrumento = []
            integrante = input("Nome integrante: ")
            instrumento = ' '
       
    
            while instrumento != '':
                instrumento = input("Instrumento: ")
                if instrumento != '':
                    lista_instrumento.append(instrumento)
            tupla = (integrante,lista_instrumento)
            lista_integrantes.append(tupla)
        dic[nome] = [ano,[lista_integrantes]]

def alterar_dados(dic,nome):
    if nome in dic:
        novo_ano = int(input("Novo ano: "))
        dic[nome][0] = novo_ano
        
        lista_integrantes =[]
        n = int(input("Número de integrantes: "))
        for i in range(n):
            lista_instrumento = []

            integrante = input("Nome integrante: ")
            instrumento = ' '
    
            while instrumento != '':
                instrumento = input("Instrumento: ")
                if instrumento != '':
                    lista_instrumento.append(instrumento)
            tupla = (integrante,lista_instrumento)
            lista_integrantes.append(tupla)
        dic[nome] = [novo_ano,[lista_integrantes]]
    else:
        print("Banda não encontada")

def exibir_dados(dic,nome):
    if nome in dic:
        for chave,valor in dic.items():
            if chave == nome:
                print(nome)
                print(f"Ano: {dic[chave][0]}")
                for dados in dic[chave][1]:
                    print(dados, end = " ")
    else:
        print("Banda não encontrada!")

def exibir_integrante(dic, nome_inst):
    lista = []
    for banda, dados in dic.items():
        integrantes = dados[1][0]
        
        for nome,instrumentos in integrantes:
            tupla = ()
            if nome_inst in instrumentos:
                tupla = (banda, nome)
                lista.append(tupla)
    return lista

def maior_banda(dic):
    l = []
    maior = 0
    for banda,dados in dic.items():
        cont = 0
        integrantes = dados[1][0]

        for nome in integrantes:
            cont += 1
        if cont > maior:
            maior = cont
            l=[banda]
        elif cont == maior:
            l.append(banda)

    return l

def gravar_arquivo (dic):
    ref_arq=open("Bandas.txt",'w')
    if len(dic):
        for banda in dic:
           valor=dic[banda]
           linha= banda + '*' + str(valor[0]) + '*' 
           integrantes=valor[1][0]
           for tupla in integrantes:
               linha= linha + tupla[0] + "#"
               for instrumento in tupla[1]:
                   linha= linha + instrumento + "&"
               linha=linha[:-1]
               linha=linha + "$"            
           linha = linha + '\n'
           #print(linha)
           ref_arq.write(linha)
    ref_arq.close()

def carrega_bandas(dic):
    ref_arq=open("Bandas.txt",'r')
    for linha in ref_arq:
        linha=linha[:len(linha)-2]
        dados=linha.split("*")
        banda=dados[0]
        ano=int(dados[1])
        lista=dados[2]
        integrantes=lista.split("$")
        lista=[]
        for membro in integrantes:
            membro=membro.split("#")
            integrante=membro[0]
            instrumentos=membro[1].split("&")
            tupla=(integrante, instrumentos)
            lista.append(tupla)
        dic[banda]=[ano, [lista]]
    ref_arq.close()
    #print(dic)


opcao = 0
while opcao != 6 :
    print("[1]- Inserir banda")
    print("[2]- Alterar dados")
    print("[3]- Exibir dados")
    print("[4]- Exibir integrante")
    print("[5]- Maior banda")
    print("[6]- Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        inserir_banda(Bandas)
        gravar_arquivo(Bandas)
    elif opcao == 2:
        Nome = input("Nome: ")
        alterar_dados(Bandas,Nome)
        gravar_arquivo(Bandas)
    elif opcao == 3:
        Nome = input("Nome: ")
        exibir_dados(Bandas, Nome)
        carrega_bandas(Bandas)
    elif opcao == 4:
        Nome_list = input("Nome: ")
        exibir_integrante(Bandas,Nome_list)
        carrega_dados(Bandas)
    elif opcao == 5:
        print(maior_banda(Bandas))
        carrega_bandas(Bandas)
                
        
