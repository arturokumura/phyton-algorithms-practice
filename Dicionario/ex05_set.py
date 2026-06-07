'''5. Uma empresa realizou três eventos de capacitação para seus funcionários. Os
participantes de cada evento foram armazenados em listas contendo os
respectivos códigos dos funcionários.'''
evento_python = [101, 105, 110, 115, 120, 125, 130]
evento_sql = [105, 110, 120, 135, 140, 145]
evento_redes = [101, 110, 125, 140, 150]
'''
Utilizando conjuntos (set), desenvolva um programa que determine:
a) Quantos funcionários participaram de pelo menos um evento.
b) Quais funcionários participaram dos três eventos.
c) Quais funcionários participaram de Python, mas não participaram de SQL.
d) Quais funcionários participaram de exatamente um dos eventos.
e) Exiba os resultados em ordem crescente'''

def ordem(l):
    for i in range(len(l)):
        menor = i
        for j in range(i+1,len(l)):
            if l[j] < l[menor]:
                menor = j
        aux = l[i]
        l[i] = l[menor]
        l[menor] = aux
    return l
#A
cont = 0
eventos = set(evento_python + evento_sql + evento_redes)
for ev in eventos:
    cont += 1
print(cont , "participaram de pelo menos um evento")

#B
a = set(evento_python)
b = set(evento_sql)
c = set(evento_redes)

res = set(c.intersection(a,b))
print(ordem(list(res)))
#C
res = a-b
print(ordem(list(res)))

#D
total = a.union(b,c)
d = []
for f in total:
    cont = 0
    if f in evento_python:
        cont += 1
    if f in evento_sql:
        cont += 1
    if f in evento_redes:
        cont += 1
    if cont == 1:
        d.append(f)
print(ordem(list(d)))





