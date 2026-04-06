#Inicializações
frase = input("Digite uma frase: ")
letra = input("Letra a ser retirada da frase: ")
nova = ""
pos = 0

#Percorrer a string 
for i in range(len(frase)):
    if frase[i] == letra:
        pos = i
        
#Juntar tudo sem a primeira ocorrência da letra
nova = nova + frase[:pos] + frase[pos + 1:]
print(nova)
