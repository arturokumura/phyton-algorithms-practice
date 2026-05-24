'''Considere que uma pessoa tem um conjunto de lápis com 10 tons diferentes de uma mesma cor,
numerados de 0 a 9. Numa fita quadriculada, alguns quadrados foram coloridos inicialmente
com o tom 0. A pessoa precisa determinar, para cada quadrado não colorido (indicado por -1),
qual é a distância dele para o quadrado mais próximo de tom 0. A distância entre dois quadrados
é definida com o número mínimo de movimentos para a esquerda, ou para a direita, para ir de
um quadrado para o outro. O quadrado não colorido, então, deve ser colorido com o tom cuja
numeração corresponde à distância determinada. Se a distância for maior ou igual a 9, o
quadrado deve ser colorido como o tom 9. Faça uma função que receba como parâmetro a lista
com os quadrados não coloridos (-1) e retorne a fita colorida. Sempre haverá pelo menos um “0”
inicialmente na fita. A fita retornada deve ser mostrada no programa principal de modo
formatado.'''
fita = [-1 ,0, -1 ,-1 ,-1 ,-1, -1 ,-1, -1 ,-1, 0 ,-1, -1]

for i in range(len(fita)):

    if fita[i] == -1:

        menor = 999

        for j in range(len(fita)):

            if fita[j] == 0:

                if i > j:
                    distancia = i - j
                else:
                    distancia = j - i

                if distancia < menor:
                    menor = distancia

        if menor >= 9:
            fita[i] = 9
        else:
            fita[i] = menor

print(fita)
