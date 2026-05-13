'''Faça uma função que recebe uma lista de números reais e retorna o valor do menor
elemento e sua posição na lista. Não é permitido o uso de qualquer função que não
seja da sua autoria.'''
def menorl(l):
    menor = l[0]
    pos = 0
    for i in range(len(l)):
        if l[i] < menor:
            menor = l[i]
            pos = i + 1
    return menor,pos

print("---------Menor-----------")
n = int(input("Tamanho da lista: "))
lista = []
for i in range(n):
    v = int(input("Número: "))
    lista.append(v)
valor, ind = menorl(lista)
print(f"Menor valor: {valor} e seu indice: {ind}")
