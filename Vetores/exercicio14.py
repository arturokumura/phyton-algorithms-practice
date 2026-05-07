'''14. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X e remova todas as ocorrências desse número
da lista. Mostre a lista resultante.
○ A respeito de funções de lista, só é permitido o uso da função append(), len() e del()'''

N = int(input("Quantos valores serão lidos? "))
lista = []
resultado = []
for i in range(N):
    n = int(input("Infome um valor: "))
    lista.append(n)
x = int(input("Infome um valor a ser removido: "))
cont = 0

for j in range(len(lista)):
    if lista[j] != x:
        cont += 1
        if cont == len(lista):
            print("Informe um número da lista!")
        resultado.append(lista[j])
print(resultado)
