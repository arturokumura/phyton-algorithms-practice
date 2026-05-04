'''3. Faça um programa que leia dados de temperatura durante uma semana (7 leituras),
armazenando em uma lista. Após ter criado a lista, escreva quantos dias dessa semana a
temperatura esteve acima da média.'''
temperaturas = []
for i in range(7):
    temp = float(input("Informe a temperatura: "))
    temperaturas.append(temp)

#media
total =  0
for t in temperaturas:
    total += t
media = total / 7

#verificar
cont = 0
for c in temperaturas:
    if c > media:
        cont += 1
print(f"Número de dias da semana com temperatura acima da média ({media}) é {cont}")
