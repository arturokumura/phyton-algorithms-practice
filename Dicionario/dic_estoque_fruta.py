dic_estoque_frutas = {'banana': 50, 'laranja':12}
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

