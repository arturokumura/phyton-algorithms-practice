'''Faça uma função que recebe uma lista de números reais e retorna o valor do maior
elemento e sua posição na lista. Não é permitido o uso de qualquer função que não
seja da sua autoria.'''
def maiorn(l):
    maior = l[0]
    pos = 0
    for i in range(1,len(l)):
        if l[i] > maior:
           maior = l[i]
           pos = i + 1
    return maior,pos

print("------------Lista--------------")
n = int(input("Tamanho da lista: "))
lista = []
for i in range(n):
    v = float(input("Número: "))
    lista.append(v)
valor,indice = maiorn(lista)
print("Maior elemento: ", valor)
print("Posiçao: " , indice)
