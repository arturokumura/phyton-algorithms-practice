'''6. Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X. Ao fim escreva se o elemento está na lista ou
não.
○ A respeito de funções de lista, só é permitido o uso da função append() e len()'''

lista = []
N = int(input("Informe um número: "))
X = int(input("Verificar se este numero esta na lista: "))
for i in range(N):
    valor = int(input("Informe um valor: "))
    lista.append(valor)
print(f"Lista: {lista}")
achou = False
for j in range(len(lista)):
    if lista[j] == X and not achou:
        print(f"O número {X} está na lista")
        achou = True
    elif lista[j] != X and not achou:
        print(f"O número {X} não está na lista")
        achou = True
    
