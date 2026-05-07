'''12. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X e remova a primeira ocorrência desse número
da lista. Mostre a lista resultante.
○ A respeito de funções de lista, só é permitido o uso da função append(), len() e del()'''
N = int(input("Quantos números ler? "))
x = int(input("Informe um número para remover: "))
lista = []
resultado = []
pos = 0
parar = False
cont = 0
for i in range(N):
    n = int(input("Leia um número: "))
    lista.append(n)

for j in range(len(lista)):
    if lista[j] == x and not parar:
        pos = j
        resultado = lista[:pos] + lista[pos + 1:]
        parar = True
    elif lista[j] != x:
        cont += 1
        if cont == len(lista):
            print("Número não presente na lista")
print(resultado)


