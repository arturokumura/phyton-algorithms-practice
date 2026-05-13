''' Faça uma função que recebe uma lista de números reais e retorna o valor da média
entre seus elementos. Não é permitido o uso de qualquer função que não seja da
sua autoria. '''
def medial(l):
    soma = 0
    for c in l:
        soma += c
    media =  soma / len(l)
    return media
print("-----------Média-------------")
n = int(input("Tamanho da lista: "))
lista = []
for i in range(n):
    v = int(input("Número: "))
    lista.append(v)
print("Média: " , medial(lista))
