#Durante uma corrida de automóveis com 10 voltas de duração foram
#anotados para um piloto, na ordem, os tempos registrados em cada volta.
#Faça um programa que leia o tempo de cada volta, calcule e mostre:
# o melhor tempo;
# a volta de melhor tempo;
# o tempo médio das 10 voltas.
#OBS: tempo da volta será indicado em segundos
soma_tempo = 0
menor = 99999999
for n in range(1,11):
    volta = int(input("Número da volta: "))
    tempo = int(input("Tempo: "))
    soma_tempo += tempo
    if(tempo < menor):
        menor = tempo
        melhor_volta = n
media = soma_tempo / 10
print(f"O melhor tempo foi {menor}")
print(f"A melhor volta foi a {melhor_volta}°")
print(f"Tempo médio das voltas: {media}")
