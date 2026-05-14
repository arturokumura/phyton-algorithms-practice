'''Faça uma função que recebe uma lista de números reais e retorna a lista ordenada
do menor para o maior valor. Não é permitido o uso de qualquer função que não
seja da sua autoria. '''
#Selection sort
def ordenarl(l):
    for i in range(len(l)-1):
        menor = i
        x = l[i]
        
        for j in range(i +1, len(l)):
            if l[j] < x:
                menor = j
                x = l[j]
        l[menor] = l[i]
        l[i] = x
    return l

print("-------------Lista--------------")
n = int(input("Tamanho: "))
lista = []
for i in range(n):
    v = int(input("Número: "))
    lista.append(v)
print(ordenarl(lista))
