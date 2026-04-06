''''● Faça um programa que leia uma frase e mostre a posição da última ocorrência de
uma letra informada pelo usuário na frase.
● Entradas: frase e letra a ser encontrada (última ocorrência da esquerda para a direita
'''
frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

#Posicao de referencia
posicao = -1

for i in range(len(frase)):
    if letra == frase[i]:
     posicao = i
print(posicao)    
  
