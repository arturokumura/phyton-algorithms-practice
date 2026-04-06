frase1 = "Boa noite com melodia"
frase2  = frase1[:14] + "alegria!"
print(frase2)

print("---------------------------------")

frase1 = "Boa noite com melodia"
frase2 = ""
for i in range(14):
    frase2 = frase2 + frase1[i]
frase2 += "alegria!"
print(frase2)
