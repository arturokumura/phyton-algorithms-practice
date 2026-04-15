'''8. Dada uma string no formato de compressão anterior (exemplo: "a3b2c1"), reconstrua a string original.'''

s = input("Digite a string: ")
resultado = ""

for i in range(0, len(s), 2):
    letra = s[i]
    quantidade = int(s[i+1])
    
    for j in range(quantidade):
        resultado += letra

print(resultado)
