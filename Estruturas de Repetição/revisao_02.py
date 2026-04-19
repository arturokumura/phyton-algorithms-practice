'''Fazer um programa que leia um conjunto de valores correspondentes às notas que alunos obtiveram
em uma prova. Quando o valor fornecido for um número negativo, significa que não existem mais
notas a serem lidos. Após isso seu programa deverá:
 escrever o número de alunos;
 escrever a maior nota;
 escrever a menor nota;
 escrever a média geral da sala'''

n = int(input("Ler nota? (-1 --> parar): "))
alunos = 0
maior = 0
total_notas = 0
menor = 10
while n > 0:
    nota = int(input("Nota: "))
    alunos += 1
    total_notas += nota
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    n = int(input("Ler nota? (-1 --> parar): "))
media = total_notas / alunos
print(f"Números de alunos: {alunos}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média da sala: {media}")
    
