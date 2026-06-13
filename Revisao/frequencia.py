

frase = input("Digite uma frase: ")
#Criar dicionario
dicionario = {}

for letra in frase:
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
        dicionario[letra] +=1

#Verificar maior
maior = 0
for letra, frequencia in dicionario.items():
    if frequencia > maior:
        maior = frequencia
        letra_mais_frequente = letra
print(f"Letra: {letra_mais_frequente}|| frequência: {maior}")

        
