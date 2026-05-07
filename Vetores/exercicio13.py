'''13. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X e remova a última ocorrência desse número da
lista. Mostre a lista resultante.
○ A respeito de funções de lista, só é permitido o uso da função append(), len() e del()
'''
N = int(input("Informe quantos valores sera lido: "))
x = int(input("Informe um valor a ser removido: "))
lista = []
resultado = []
pos = 0
for i in range(N):
    n = int(input("Informe um valor: "))
    lista.append(n)

for j in range(len(lista)):
    if lista[j] == x:
        pos = j
        resultado = lista[:pos] + lista[pos+1:]
print(resultado)
