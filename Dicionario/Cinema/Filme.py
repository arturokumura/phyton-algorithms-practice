Filme = {('Guardiões da Galaxia', 2018): [1200000, 'James Gunn',['Chris Pratt', 'Vin Diesel','Karen Gilan']],
('Bad Boys 1', 2008): [3420000, 'Michael Bay', ['Will Smith', 'Jacob Scipio', 'Eric Dane']]}

def inserir_filme(filme):
    nome = input("Nome: ")
    for chave in filme.keys():
        if nome in chave:
            return -1
    else:
        ano = int(input("Ano de lançamento: "))
        custo = float(input("Custo: "))
        diretor = input("Diretor: ")
        atores = []
        ator = input("Ator(a): ")
        while ator != '':
            atores.append(ator)
            ator = input("Ator(a): ")
            
        tupla = (nome,ano)
        lista = [custo,diretor,atores]
        filme[tupla]  =lista
        return filme

def alterar_filme(filme):
    nome = input("Nome: ")
    for chave,valor in filme.items():
        if nome not in chave:
            return -1
        else:
            lista = valor
    
        print("-------Possíveis alterações-------")
        print("Custo")
        print("Diretor")
        print("Atores")
        alterar = input("Alterar: ")
        if alterar.lower() == 'custo':
            novo_custo = input("Custo: ")
            lista[0] = novo_custo
        elif alterar.lower() == 'diretor':
            novo_diretor = input("Diretor: ")
            lista[1] = novo_diretor
        elif alterar.lower() == 'atores':
            novo_atores = []
            ator = input("Ator(a): ")
            while ator != '':
                novo_atores.append(ator)
                ator = input("Ator(a): ")
            lista[2] = novo_atores
        else:
            return -2
    for chave,valor in filme.items():
        if nome in chave:
            filme[chave] = lista
    return filme

def excluir_filme(filme):
    nome = input("Nome: ")
    for chave,valor in filme.items():
        if nome in chave:
            confirm = input("Confirmar alteração?(s/n): ")
            if confirm.lower() == 's':
                del filme[chave]
                return filme
            else:
                return -1
    return -2

def listar_filme(filme):
    nome = input("Nome: ")
    for chave,valor in filme.items():
        if nome in chave:
            print("---------", chave[0] , "---------")
            print(f"Ano de lançamento: {chave[1]}")
            print(f"Custo de produção: {valor[0]}")
            print(f"Diretor: {valor[1]}")
            print("Atores: ")
            for ator in valor[2]:
                print(ator)
            print("-------------------------------")
    return -1
        
def listar_filmes(filme):
    for chave,valor in filme.items():
        print("-------------------------")
        print(f"     {chave[0]}         ")
        print(f"Ano de lançamento: {chave[1]}")
        print(f"Custo de produção: {valor[0]}")
        print(f"Diretor: {valor[1]}")
        print("Atores: ")
        for ator in valor[2]:
            print(ator)
        print()

def gravar_arquivo(filme):
    ref_arq = open('Filme.txt', 'w')
    for chave,valor in filme.items():
        linha = chave[0]+'*'+str(chave[1])+'%'+str(valor[0])+ '$'+ valor[1] + '&'
        for v in valor[2]:
            linha += v + '#'
        linha += '\n'
        ref_arq.write(linha)
    ref_arq.close()

def ler_arquivo(filme):
    ref_arq = open('Filme.txt','r')
    for linha in ref_arq:
        linha = linha[:len(linha)-2]
        nome,resto = linha.split('*')
        ano,resto  = resto.split('%')
        custo,resto = resto.split('$')
        diretor,resto = resto.split('&')
        atores =  []
        resto = resto.split('#')
        for v in resto:
            atores.append(v)
        filme[(nome,int(ano))] = [float(custo),diretor,atores]
    return filme
        
    
opcao = -1
while opcao != 7:
    print("[1]- Inserir filme")
    print("[2]- Alterar dados")
    print("[3]- Excluir filme")
    print("[4]- Listar filme")
    print("[5]- Listar filmes")
    print("[6]- Ler dados (arquivo)")

    opcao = int(input("Opção: "))
    if opcao == 1:
        res = inserir_filme(Filme)
        if res == -1:
            print("Filme já cadastrado!")
        else:
            print(res)
    elif opcao == 2:
        res = alterar_filme(Filme)
        if res == -1:
            print("Filme não encontrado!")
        elif res == -2:
            print("Dado não encontrado!")
        else:
            print(res)
    elif opcao == 3:
        res = excluir_filme(Filme)
        if res == -1:
            print("Exclusão cancelada!")
        elif res == -2:
            print("Filme não encontrado!")
        else:
            print(res)
    elif opcao == 4:
        res = listar_filme(Filme)
        if res == -1:
            print("Filme não encontrado!")
        else:
            listar_filme(Filme)
    elif opcao == 5:
        listar_filmes(Filme)
    elif opcao == 6:
        print(ler_arquivo(Filme))

    gravar_arquivo(Filme)
