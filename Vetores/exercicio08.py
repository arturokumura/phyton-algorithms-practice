'''8. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Ao fim escreva o maior valor encontrado e sua posição na lista.
○ A respeito de funções de lista, só é permitido o uso da função append() e len()'''
N = int(input("Quantos números ler? "))
lista = []
maior = 0
for i in range(N):
    valor = int(input("Informe um valor: "))
    lista.append(valor)

for j in range(len(lista)):
    if lista[j] > maior:
        maior = lista[j]
        pos = j
print(f"Maior valor encontrado é: {maior}, na posição {pos}")
                
