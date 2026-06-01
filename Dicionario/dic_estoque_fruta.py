'''dic_estoque_frutas = {'banana': 50, 'laranja':12}
print(dic_estoque_frutas)
dic_estoque_frutas["melancia"]=7
print(dic_estoque_frutas)
dic_estoque_frutas["melancia"]=9

for fruta in dic_estoque_frutas:
    chave = fruta
    valor = dic_estoque_frutas[chave]
    print("Temos %d items do elemento %s no estoque."%(valor,chave))
print("----------------------------------------------")
for fruta in dic_estoque_frutas.keys():
    chave = fruta
    valor = dic_estoque_frutas[chave]
    print("Temos %d items do elemento %s no estoque."%(valor,chave))
print("----------------------------------------------")
total = 0
for valor in dic_estoque_frutas.values():
    total += valor
print(f"Temos {total} frutas no estoque")
print("----------------------------------------------")
for k in dic_estoque_frutas.items():
    print(f"Par Chave-Valor", k)
print("----------------------------------------------")
ks = list(dic_estoque_frutas.keys())
ks.append('Kiwi')
print("Lista de frutas: ",ks)

for k in ks:
    print(k, ": ", dic_estoque_frutas.get(k,"Não tem"))
print("------------------------------------------------")
#Cópias
d1 = {"Catarina":5}
d2 = d1
print(d2 is d1)
d1["Jonas"] = 20
print(d2)

d1 = {"Joao": 10, "Maria": 20}
d2 = d1.copy()
d2["Pedro"] = 30
d1["Joao"] = 40
print(d1)
print(d2)'''

#Limpar
idades =  {"Joao":10, "Maria":12}
print("id(idades):", id(idades))

idadesCriancas = idades
print("Id(idadesCriancas):", id(idadesCriancas))

idades = {}
print("id(idades) após a reatribuição:", id(idades))
print("Idades:", idades)
print("idadesCriancas:", idadesCriancas)

