'''Desenvolva um jogo da forca. O programa deverá ter várias listas já montadas pelo
programador, sendo uma lista de Temas (países, animais, frutas, filmes, etc.) e uma lista
de opções correspondentes para cada um dos temas. O programa, a cada execução,
deverá gerar um número aleatório que definirá o tema (índice da lista de temas) e um
segundo número aleatório para pegar a palavra (índice da respectiva palavra do tema
específico sorteado. A partir da seleção de uma palavra o jogador poderá errar 6 vezes
antes de ser enforcado. O seu programa deve receber uma letra do usuário por vez e
comparar com a palavra escolhida, além disso é interessante desenvolver uma pequena
interface, cujas letras inicialmente sejam colocadas com “_”, conforme as letras forem
sendo informadas corretamente é feita a substituição no lugar do underline. Veja o
exemplo:
'''

temas = ["Países", "Animais", "Frutas"]

paises = ["brasil", "canada", "japao"]
animais = ["gato", "cachorro", "elefante"]
frutas = ["banana", "manga", "abacaxi"]

print("---------Jogo da Forca----------")
print("[1] - Países")
print("[2] - Animais")
print("[3] - Frutas")
tema = int(input("Escolha um tema: "))
palavra = int(input("Escolha uma palavra(1/2/3): "))

if tema == 1:
    escolhida = paises[palavra -1]
elif tema == 2:
    escolhida = animais[palavra -1]
else:
    escolhida = frutas[palavra -1]

# Cria a palavra escondida com "_"
forca = []
for i in range(len(escolhida)):
    forca.append("_")

erros = 0

# Jogo principal
while erros < 6 and "_" in forca:
    print()
    
    # Mostra o tema
    print("Tema:", temas[tema - 1])

    # Mostra a palavra atual
    for letra in forca:
        print(letra, end=" ")
    print()

    print("Erros:", erros, "/ 6")

    chute = input("Digite uma letra: ").lower()

    acertou = False

    # Procura a letra na palavra escolhida
    for i in range(len(escolhida)):
        if escolhida[i] == chute:
            forca[i] = chute
            acertou = True

    # Se não encontrou, conta erro
    if not acertou:
        erros += 1

# Resultado final
print()

if "_" not in forca:
    print("Parabéns! Você acertou a palavra:", escolhida.upper())
else:
    print("Você foi enforcado!")
    print("A palavra era:", escolhida.upper())
    
