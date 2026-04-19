'''Durante uma corrida de automóveis com 10 voltas de duração foram anotados para um piloto, na
ordem, os tempos registrados em cada volta. Faça um algoritmo que leia o tempo de cada volta, calcule
e mostre:
 o melhor tempo;
 a volta de melhor tempo;
 o tempo médio das 10 voltas.
OBS: tempo da volta será indicado em segundos.'''

n = 10
pos = 0
total = 0
i = 1
for i in range(10):
    tempo = float(input("Tempo: "))

    total += tempo
    if i == 0:
        menor = tempo
        pos = i + 1
    else:
        if tempo < menor:
            menor = tempo
            pos = i + 1
media = total / 10
print(f"Melhor tempo: {menor}s")
print(f"A {pos}° foi a melhor volta")
print(f"Média das voltas: {media}")
