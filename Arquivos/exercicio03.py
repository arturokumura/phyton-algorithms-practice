loja= Loja= [
[ 1, "Camiseta" , [19.99, 50] ],
[ 2, "Tênis" , [49.99, 30] ],
[ 3, "Boné" , [9.99, 100] ]
]

def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

def verificar_produto(loja,p):
    for produto in loja:
        if produto[1] == p:
            return True
    return False


def inserir_produto(loja):
    codigo = int(input("Código: "))

    # Verifica se o código já existe
    for produto in loja:
        if produto[0] == codigo:
            print( "Erro: código já cadastrado!")
            return

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quantidade em estoque: "))

    novo_produto = [codigo, nome, [preco, estoque]]
    loja.append(novo_produto)

    print("Produto cadastrado com sucesso!")

def venda(loja, cod, quant_vendida):
    for produto in loja:
        if produto[0] == cod:

            if quant_vendida > produto[2][1]:
                return "Impossível realizar a venda"

            produto[2][1] -= quant_vendida

            preco_final = quant_vendida * produto[2][0]

            return preco_final

    return "Produto não encontrado"
    if not achou :
        return 'Código inválido!'


def quantidade_iguais(loja,num_q):
    produtos= []
    achou = False
    for i in range(len(loja)):
        if loja[i][2][1]<= num_q:
            produtos.append(loja[i][1])
            achou = True
            
    if not achou :
        print("Nenhum produto encontrado!")
    for p in produtos:
        print(p)

def atualizar_preco(loja,cod,valor):
    achou = False
    for i in range(len(loja)):
        if loja[i][0] == cod:
            achou = True
            loja[i][2][0] = valor
    if not achou:
        print("Código inválido!")

def listar(loja):
    for produto in loja:
        print(produto)
def gravar_dados(loja):
    if len(loja):
        ref_arq = open("produtos1.txt",'w')
        for produto in loja:
            linha =  str(produto[0]) + "\t"+ str(produto[1]) +"\t"+ str(produto[2]) + "\n"
            ref_arq.write(linha)
    elif len(loja) == 0:
        print("Lista vazia!")
    ref_arq.close()

def ler_dados(loja):
    if Existe_Arquivo("produtos1.txt"):
        ref_arq = open("produtos1.txt",'r')
        for linha in ref_arq:
            linha = linha[:-1]
            produto = linha.split("\t")
            loja.append(produto)
        ref_arq.close()
    else:
        print("Arquivo não encontrado!")
            
opcao = ''
ler_dados(loja)
while opcao != 6:
    print("[1]- Inserir produto")
    print("[2]- Efetuar venda")
    print("[3]- Exibir produtos abaixo do estoque mínimo")
    print("[4]- Alterar preço de produto")
    print("[5]- Mostrar todos os produtos (formatado)")
    print("[6]- Fim")
    opcao = int(input("Opção: "))

    if opcao == 1:
        inserir_produto(loja)
    elif opcao == 2:
        codigo = int(input("Código: "))
        quantidade_vendida =int(input("Quntidade vendida: "))
        print(venda(loja,codigo,quantidade_vendida))
    elif opcao == 3:
        estoque_min = int(input("Estoque mínimo: "))
        quantidade_iguais(loja,estoque_min)
    elif opcao == 4:
        codigo = int(input("Código: "))
        novo_p = float(input("Novo preço: "))
        atualizar_preco(loja,codigo,novo_p)
    elif opcao == 5:
        listar(loja)
    elif opcao == 6:
        gravar_dados(loja)
    
    
    
    
