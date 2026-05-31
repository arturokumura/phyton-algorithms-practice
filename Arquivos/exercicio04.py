#a) programa que retorna o nome do estudante que possui mais de 6 notas;
arq = open("estudantes.dat", "r")
for linha in arq:
    aluno = linha.split()
    nome = aluno[0]
    notas = []
    for nota in aluno[1:]:
        notas.append(int(nota))

    # a)
    if len(notas) > 6:
        print("Mais de 6 notas:", nome)

    # b)
    media = sum(notas) / len(notas)
    print("Média de", nome, "=", round(media, 2))

    # c)
    print("Menor nota:", min(notas))
    print("Maior nota:", max(notas))
    print()

arq.close()
