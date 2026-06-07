'''
e) Crie um novo dicionário em que a chave seja o código do aluno e o valor seja um conjunto contendo os
livros que ele retirou.'''
emprestimos = {
 "L001": [10, 15, 20, 25, 30],
 "L002": [15, 20, 35, 40],
 "L003": [10, 20, 25, 45],
 "L004": [15, 30, 35, 50]
}
#a
cont = 0
l1 = set(emprestimos['L001'])
l2 = set(emprestimos['L002'])
l3 = set(emprestimos['L003'])
l4 = set(emprestimos['L004'])
res = l1.union(l2,l3,l4)
for i in res:
    cont += 1
print(cont)
#b
l = []
for aluno in res:
    cont = 0
    for leitores in emprestimos.values():
        if aluno in leitores:
            cont += 1
    if cont >= 2:
        l.append(aluno)
print(l)
#c
res = l1.intersection(l2,l3,l4)
print(res)
#d
t1 = len(l1)
t2 = len(l2)
t3 = len(l3)
t4 = len(l4)
tamanho = []
tamanho= [t1,t2,t3,t4]
maior = 0
for t in tamanho:
    if t > maior:
        maior = t
for chave,valor in emprestimos.items():
    if len(valor) == maior:
        print(chave)

#e
total = l1.union(l2,l3,l4)
dic = {}
for leitores in total:
    l = []
    for chave,valor in emprestimos.items():
        if leitores in valor:
            l.append(chave)
            dic[leitores] = set(l)
for aluno in sorted(dic):
    print(aluno, dic[aluno])

