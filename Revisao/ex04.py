'''Para uma string de entrada, substitua cada letra pelo seu "espelho" no alfabeto (por exemplo, 'a' → 'z', 'b' →
'y', ..., 'z' → 'a').'''
s = input("Informe uma string: ")
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_invertido = ""

#Inverter alfabeto
for letra in range(len(alfabeto) -1, -1, -1):
       alfabeto_invertido += alfabeto[letra]
resultado = ""

for c in s:
    pos= 0
#Achar posicao da letra
    for j in range(len(alfabeto)):
       if alfabeto[j] == c:
           pos = j


    nova= alfabeto_invertido[pos]
    resultado += nova
print(resultado)
