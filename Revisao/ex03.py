'''. Receba duas strings de mesmo tamanho e intercale seus caracteres de forma cíclica, de modo que os caracteres
da primeira string apareçam em posições ímpares e os da segunda, em pares.'''

s1 = input("Digite a primeira: ")
s2 = input("Digite a segunda: ")

resultado = ""

for i in range(len(s1)):
    # Adiciona caractere de s1 (posição ímpar no resultado: index 0, 2, 4...)
    resultado += s1[i]
    # Adiciona caractere de s2 (posição par no resultado: index 1, 3, 5...)
    resultado += s2[i]

print(f"Resultado intercalado: {resultado}")


