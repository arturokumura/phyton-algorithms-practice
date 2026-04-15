'''9. Para cada caractere da string, desloque-o no alfabeto de acordo com sua posição na string (0 → não muda, 1 →
desloca 1 posição, 2 → desloca 2 posições, etc.), respeitando os limites do alfabeto, de forma circular (voltando ao
início). Exemplo: “eu amo abacaxi” → “ev dqt hjjmljv”'''

s = input("Digite a frase: ")
alfabeto = "abcdefghijklmnopqrstuvwxyz"

resultado = ""
pos = 0

for i in range(len(s)):
    c = s[i]
    
    if c == " ":
        resultado += " "
    else:
        # achar posição da letra
        for j in range(len(alfabeto)):
            if c == alfabeto[j]:
                pos = j
        
        # deslocamento correto (usar i!)
        nova_pos = pos + i
        
        while nova_pos >= 26:
            nova_pos -= 26
        
        resultado += alfabeto[nova_pos]

print(resultado)
        

