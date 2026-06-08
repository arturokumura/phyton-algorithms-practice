voo1 = [
 ('111', 'Ana'),
 ('222', 'Carlos'),
 ('333', 'Mariana'),
 ('444', 'Pedro')
]
voo2 = [
 ('222', 'Carlos'),
 ('333', 'Mariana'),
 ('555', 'Lucas'),
 ('666', 'Fernanda')
]

voo3 = [
 ('111', 'Ana'),
 ('333', 'Mariana'),
 ('777', 'Patricia'),
 ('888', 'Rob')]

'''a) Quantos passageiros distintos viajaram na semana;
b) Quais passageiros viajaram em mais de um voo;
c) Quais passageiros viajaram nos três voos;
d) Quais passageiros viajaram apenas uma única vez;
e) Crie um dicionário onde a chave seja o CPF e o valor seja a quantidade de voos realizados;
f) Determine qual passageiro realizou o maior número de voos e exiba seu nome e quantidade de viagens.'''

v1= set(voo1)
v2 = set(voo2)
v3 = set(voo3)

#a
distintos = v1 | v2| v3
print("Passageiros distintos: ")
print(len(distintos))


#b
total = voo1 + voo2 + voo3
d ={}
for cpf,nome in total:
    if nome in d:
        d[nome] += 1
    else:
        d[nome] = 1
passageiros = []
for nome, quant in d.items():
    if quant > 1:
        passageiros.append(nome)
print("Passageiros em mais de unm voo:")
for nomes in passageiros:
    print(nomes)

#c
res = v1.intersection(v2,v3)
print("Passageiros que viajaram nos tres voos: ")
print(res)

#d
contagem = {}

for cpf, nome in voo1 + voo2 + voo3:
    if cpf not in contagem:
        contagem[cpf] = 1
    else:
        contagem[cpf] += 1
for cpf , quant in contagem.items():
    if quant == 1:
        print(cpf)

#e
print(contagem)

#f
maior = 0
l =[]
for cpf,quant in contagem.items():
    if quant > maior:
        maior = quant
        l = [cpf,quant]
    elif quant == maior:
        l.append([cpf,quant])
quant = l[1]
print(l)
for c in l:
    for nomes in voo1:
        if nomes[0] == c:
            l = [nomes]
for dados in l:
    name = dados[1]
print(name,quant)
