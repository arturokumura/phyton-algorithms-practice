'''11. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Ao fim escreva qual número aparece mais vezes na lista, considerando a
possibilidade de empate.
○ A respeito de funções de lista, só é permitido o uso da função append() e len()
'''
N = int(input("Quantos números ler? "))

lista = []

for i in range(N):
    num = int(input("Informe um valor: "))
    lista.append(num)

maior = 0
resultado = []

for c in lista:
    cont = 0

    for j in lista:
        if c == j:
            cont += 1

    if cont > maior:
        maior = cont
        resultado = [c]

    elif cont == maior:
        repetido = False

        for x in resultado:
            if x == c:
                repetido = True

        if repetido == False:
            resultado.append(c)

            
print("Número(s) que mais aparece(m):")

for x in resultado:
    print(x)
