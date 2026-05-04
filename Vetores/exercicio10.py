'''10. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X. Ao fim escreva o número de vezes que o
número X aparece na lista.
○ A respeito de funções de lista, só é permitido o uso da função append() e len()'''

N = int(input("Quantos valores ler? "))
X = int(input("Verificar o número: "))
lista = []
cont = 0
for i in range(N):
    num = int(input("Informe um valor: "))
    lista.append(num)

for c in lista:
    if c == X:
        cont += 1

print(f"O número {X} aparece {cont} vezes na lista")
