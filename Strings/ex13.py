'''● Utilizando a string “ Iracema – a lenda do Ceará ”, sem alterar seu valor original e sem
utilizar métodos (apenas lower() e upper() são permitidos), elabore programas que mostrem
na tela:
a) Todas as letras em maiúsculo;
b) Somente a primeira letra em maiúsculo;
c) Todas as iniciais em maiúsculo;
d) Troque os espaços em branco do início por “#” ;
e) Troque os espaços do final por “*”;
f) Retire todos os espaços em branco do início e do fim;
g) Mostre o índice da primeira ocorrência do caractere “a”:
h) Mostre o índice da última ocorrência do caractere “a”;
i) Mostre a quantidade de letras “e”;
j) Mostre a inversão de todos os caracteres (maiúsculas/minúsculas).'''

frase = " Iracema – a lenda do Ceará "

#Letras em maiúsculo
frase_maiuscula = frase.upper()

#Primeira letra em maiúsucula
primeira_letra = frase[1]
primeira_letra_maiuscula = primeira_letra.upper()

#Iniciais em maiúsuculo
frase_nov = ""
maiuscula = True

for letra in frase:
    if maiuscula and letra != " ":
        frase_nov += letra.upper()
        maiuscula = False
    else:
        frase_nov += letra
    
    if letra == " ":
        maiuscula = True

#Troque os espaços em branco do início por “#”
frase_nova1 = ""
espaco_inicio = frase[0]
espaco_inicio = "#"
frase_nova1 += espaco_inicio + frase[1:]

#Troque os espaços em branco do início por “*”
frase_nova2 = ""
espaco_final = frase[-1]
espaco_final = "*"
frase_nova2 += frase[:len(frase)-1] + espaco_final

#Retire todos os espaços em branco do início e do fim
frase_sem_espacos = ""
for c in frase:
    if c != " ":
       frase_sem_espacos += c

#Mostre o índice da primeira ocorrência do caractere “a”
indice = 0
for i in range(len(frase)-1, -1 , -1):
    if frase[i] == 'a':
        indice = i

#Mostre o índice da última ocorrência do caractere “a”
indice_2 = 0
for u in range( len(frase)):
    if frase[u] == 'a':
        indice_2 = u

# Mostre a quantidade de letras “e”
quant_letra_e = 0
for letras in frase:
    if letras == 'e':
        quant_letra_e += 1

#Mostre a inversão de todos os caracteres (maiúsculas/minúsculas)
invertida = ""
for caractere in frase:
    if caractere.islower():
        invertida += caractere.upper()
    elif caractere.isupper():
        invertida += caractere.lower()
    else:
        invertida += caractere  # mantém espaços, números, etc

#Saídas
print(f"Letras em maiúsculo: {frase_maiuscula}")
print(f"Somente a primeira letra maiúsuclo: {primeira_letra_maiuscula}")
print(f"Todas as iniciais em maiúsculo: {frase_nov}")
print(f"Trocar espaços iniciais por #: {frase_nova1}")
print(f"Trocar espaços finais por *: {frase_nova2}")
print(f"Retirar espaços do início ao fim: {frase_sem_espacos}")
print(f"Indice da primeira ocorrência do caractere 'a': {indice}")
print(f"Indice da últma ocorrência do caractere 'a': {indice_2}")
print(f"Quantidade de letras 'e': {quant_letra_e}")
print(f"Inversão dos caracteres(maiusculos/minusculos): {invertida}")
