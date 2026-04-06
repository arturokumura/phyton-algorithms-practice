'''Faça um programa que leia uma frase e retire a primeira ocorrência de uma letra
da frase
● Entradas: frase e letra a ser removida (1ª ocorrência da esquerda para a direita)
'''
#Inicializações
frase = input("Digite uma frase: ")
letra = input("Letra a ser retirada da frase: ")
nova = ""
pos = 0

#Percorrer a string de tras para frente
for i in range(len(frase)-1 ,-1, -1):
    if frase[i] == letra:
        pos = i
        
#Juntar tudo sem a primeira ocorrência da letra
nova = nova + frase[:pos] + frase[pos + 1:]
print(nova)
