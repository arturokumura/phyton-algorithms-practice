#Média de 3 notas - Lista
n = 3
s = 0
notas = []
i = 0
while i < n:
    nota = float(input("Informe a nota: "))
    s = s + nota
    notas.append(nota)
    i = i + 1
media = s / n
print(media)
i = 0
while i< n:
    if notas[i] < media:
        print("Nota", notas[i], "abaixo da média")
    i = i + 1
