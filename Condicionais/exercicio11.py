#Flíper é um tipo de jogo onde uma bolinha de metal cai por um
#labirinto de caminhos até chegar na parte de baixo do labirinto. A
#quantidade de pontos que o jogador ganha depende do caminho
#que a bolinha seguir. O jogador pode controlar o percurso da
#bolinha mudando a posição de algumas portinhas do labirinto. Cada
#portinha pode estar na posição 0, que significa virada para a
#esquerda, ou na posição 1 que quer dizer virada para a direita.
#Considere o flíper da figura abaixo, que tem duas portinhas. A
#portinha P está na posição 1 e a portinha R, na posição 0. Desse
#jeito, a bolinha vai cair pelo caminho B.
#● Você deve escrever um programa que, dadas as posições das
#portinhas P e R, neste flíper da figura, diga por qual dos três
#caminhos, A, B ou C, a bolinha vai cair.#

P = int(input("Digite a posição de P (0 ou 1): "))
R = int(input("Digite a posição de R (0 ou 1): "))

if P == 1:
    print("C")
else:
    if R == 0:
        print("A")
    else:
        print("B")
