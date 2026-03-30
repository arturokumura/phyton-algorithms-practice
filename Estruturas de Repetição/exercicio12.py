#Ler um conjunto de valores correspondentes às notas que alunos obtiveram em
#uma prova. Quando o valor fornecido for um número negativo, significa que não
#existem mais pontos para serem lidos
#○ Escrever quantas notas são maiores ou iguais a 6.0
#○ Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
#○ Escrever quantos notas são menores que 4.0

nota = int(input("Nota: "))
cont1 = 0
cont2 = 0
cont3 = 0

while (nota > 0):
    nota = int(input("Nota: "))
    if (nota >= 6.0):
        cont1 += 1
    elif (nota >= 4.0):
        cont2 += 1
    else:
        cont3 +=1

print(f"Notas maiores ou iguais a 6.0: {cont1}")
print(f"Notas maiores ou iguais a 4.0 e menores que 6.0: {cont2}")
print(f"Notas menores que 4.0: {cont3}")
