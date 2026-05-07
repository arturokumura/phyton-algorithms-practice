'''12. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X e remova a primeira ocorrência desse número
da lista. Mostre a lista resultante.
○ A respeito de funções de lista, só é permitido o uso da função append(), len() e del()'''
N = int(input("Quantos números ler? "))
lista = []
achou = False
for i in range(N):
    x = int(input("Leia um número: "))
    lista.append(x)


