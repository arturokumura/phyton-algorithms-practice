texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
texto_sem_vogais = ""

for letra in texto:
    if(letra not in vogais):
        texto_sem_vogais = texto_sem_vogais + letra
print(texto_sem_vogais)
