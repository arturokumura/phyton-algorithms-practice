'''Jogo da velha'''
tab = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(" ")
    tab.append(linha)

fim = False
while not fim:
    peca = input("Qual peca deseja posicionar? ")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    achou_pos = False

    for m in range(len(tab)):
        for n in range(len(tab[m])):
            if m == linha and coluna == n:
                tab[m][n] = peca
                achou_pos = True
    if not achou_pos:
        print("Peça não adicionada")
    #Verificar possivel vitoria dp
    vit = []
    for m in range(len(tab)):
        for n in range(len(tab[m])):
            if m == n:
                c = tab[m][n]
                vit.append(c)
    tem = True
    if vit[0] == " ":
        tem = False
    for i in range(1,len(vit)):
        if vit[i] != vit[i-1]:
            tem = False
    if tem:
        print("Vitoria na diagonal principal")
        fim = True
    #Verificar possivel vitoria ds
    vits = []
    for m in range(len(tab)):
        for n in range(len(tab[m])):
            if m + n == 2:
                vits.append(tab[m][n])
    tems = True
    if vits[0] == " ":
         tems = False
    for i in range(1, len(vits)):
        if vits[i] != vits[i-1]:
            tems = False
    if tems:
        print("Vitoria na diagonal secundária!")
        fim = True
    

    #Verificar linha:
    for m in range(len(tab)):
        vlinha = []
        for n in range(len(tab[m])):
            vlinha.append(tab[m][n])
            pos = m
        teml = True
        if vlinha[0] == " ":
            teml = False
        for i in range(1, len(vlinha)):
            if vlinha[i] != vlinha[i-1]:
                teml = False
        if teml:
            print(f"Vitoria na linha {m}")
            fim = True

    #Verificar coluna
    for n in range(len(tab[0])):
        vcoluna = []
        for m in range(len(tab)):
            vcoluna.append(tab[m][n])
            ind = m
        temc = True
        if vcoluna[0] == " ":
            temc = False
        for i in range(1, len(vcoluna)):
            if vcoluna[i] != vcoluna[i-1]:
                temc = False
        if temc:
            print(f"Vitoria na coluna {n}")
            fim = True
    #Verificar empate
    if not fim:
        cheio = True
        for linham in tab:
            for elemento in linham :
                if elemento == " ":
                    cheio = False
        if cheio:
            print("Empate!")
            fim = True
    #Imprimir tabuleiro
    for linhap in tab:
        for elemento in linhap:
            print(elemento, end = " ")
        print()
    
