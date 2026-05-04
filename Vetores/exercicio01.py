'''1. Faça um programa que leia 10 valores e armazene em uma lista. Após isso, faça:
○ Imprima todos os valores lidos
○ Imprima a soma de todos eles
○ Imprima apenas os números pares'''
lista = []
for i in range(10):
    valor = int(input("Informe um valor na lista: "))
    lista.append(valor)

#Todos os valores
print(lista)

#Soma de todos 
soma = 0
for v in lista:
    soma += v
print(soma)

#Numeros pares
for p in lista:
    if p % 2 == 0:
        print(p)
