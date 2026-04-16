'''. Implemente um algoritmo que verifica se uma string é um palíndromo perfeito ignorando espaços, pontuação e
diferenças entre particulares e minúsculos. Exemplo: "Subi no ônibus" deve retornar True.
'''
s = input("Digite uma frase: ")

acentos = "áàãâéèêìíîóòõôúùû"
sem_acento = "aaaaeeeiiioooouuu"
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

frase_limpa = ""

# 🔹 remover acentos 
for i in range(len(s)):
    
    # tenta substituir
    substituiu = 0
    for j in range(len(acentos)):
        if s[i] == acentos[j]:
            frase_limpa += sem_acento[j]
            substituiu = 1
    
    # se não substituiu, adiciona original
    if substituiu == 0:
        frase_limpa += s[i]

# 🔹 manter só letras
frase_filtrada = ""
for i in range(len(frase_limpa)):
    for j in range(len(alfabeto)):
        if frase_limpa[i] == alfabeto[j]:
            frase_filtrada += frase_limpa[i]

# 🔹 minúsculo na mão
frase_final = ""
frase_final = frase_filtrada.lower()

#Verificar palindromo
frase_final_invertida = ""
for m in range(len(frase_final) -1, -1, -1):
    frase_final_invertida += frase_final[m]
if frase_final_invertida == frase_final:
    print(True)
else:
    print(False)

