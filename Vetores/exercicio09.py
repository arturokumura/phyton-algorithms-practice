'''9. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros e
os coloque em uma lista. Ao fim escreva os elementos da lista na ordem inversa que
foram lidos.
○ A respeito de funções de lista, só é permitido o uso da função append() e len()
'''
N = int(input("Quantos valores ler? "))
lista = []
invertida = []
for i in range(N):
    valor = int(input("Informe um valor: "))
    lista.append(valor)
for j in range(len(lista)-1, -1, -1):
    invertida.append(lista[j])
print(invertida)
