vogais = "aeiou"
texto = "Instituo Federal"
for letra in texto:
    if letra.lower() in vogais:
        print(f"A letra {letra} é uma vogal!")
