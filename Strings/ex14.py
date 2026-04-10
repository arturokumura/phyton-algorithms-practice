'''● Faça um programa em Python que solicite ao usuário informar uma sequência de caracteres
e exiba as diversas sequências de letras iguais.'''

sequencia = input("Informe uma sequência de caracteres: ")

grupo = sequencia[0]  # começa com o primeiro caractere

for i in range(1, len(sequencia)):
    if sequencia[i] == sequencia[i - 1]:
        grupo += sequencia[i]  # continua o grupo
    else:
        print(grupo)  # imprime o grupo atual
        grupo = sequencia[i]  # inicia novo grupo

print(grupo)  # imprime o último grupo
    
