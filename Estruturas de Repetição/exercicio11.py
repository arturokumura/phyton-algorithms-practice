nota = int(input("Informe a nota do aluno: "))
cont = 1
maior = 0
menor = 0

while (nota >= 0):
    nota = int(input("Informe a nota do aluno: "))
    cont += 1
    if (nota > maior):
        maior = nota
    else:
        menor = nota
print(f"Número de alunos: {cont} ")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
