'''numeros = {1,2,3,2,1,4}
print(numeros)

frutas = {"maçã", "banana"}
frutas.add("uva")
frutas.add("uva")
#Remover
frutas.remove("banana")
frutas.discard("pera")'''

#Operacoes entre conjuntos
A = {1,2,3,4}
B = {3,4,5,6}
print(A | B)
print(A.union(B))

print(A & B)
print(A.intersection(B))

print(A - B)
print(A ^ B)
