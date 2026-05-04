'''7. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X. Ao fim escreva a posição na lista em que o
valor X foi encontrado. Se X não estiver na lista, escrever -1.
○ A respeito de funções de lista, só é permitido o uso da função append() e len()'''
N = int(input("Informe um numero: "))
X = int(input("Verificar na lista o número: "))
lista = []
for i in range(N):
    num = int(input("Informe um valor: "))
    lista.append(num)

cont = 0
for j in range(len(lista)):
    if lista[j] == X:
        pos = j
        print(f"O número {X} foi encontrado em: {pos}")
        cont += 1
if cont == 0:
        print(-1)
