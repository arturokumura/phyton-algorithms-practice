'''Faça uma função que recebe uma lista de números reais e retorna o valor do
produto desses números. Não é permitido o uso de qualquer função que não seja
da sua autoria.'''
def produtoLista(l):
    soma = 1
    for c in l :
        soma *= c
    return soma

print("------------Produto Lista----------")
n = int(input("Quantos numeros: "))
lista = []
for i in range(n):
    v = float(input("Número: "))
    lista.append(v)
print("Produto: ", produtoLista(lista))
