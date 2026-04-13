'''Escreva um código que receba uma string e inverta apenas os caracteres que estão em posições ímpares, trocando
os caracteres iniciais com os finais, mantendo os caracteres em posições pares inalterados. Considere que a primeira
letra da string está na posição 1. Exemplos: 123456789 → 927456381 e araraquara → rruraqaaaa
'''
'''     
string = input("Informe a string: ")


impares = ""
for i in range(len(string)):
    if (i + 1) % 2 == 1:
        impares += string[i]


impares_invertidos = ""
for i in range(len(impares) - 1, -1, -1):
    impares_invertidos = impares_invertidos + impares[i]


resultado = ""
j = 0  
for i in range(len(string)):
    if (i + 1) % 2 == 1:
        resultado = resultado + impares_invertidos[j]
        j = j + 1
    else:
        resultado += string[i]

print(resultado)'''

'''
2. Dada uma string de entrada, substitua todas as ocorrências da primeira letra pela segunda, todas da segunda pela
terceira, e assim por diante até a última ser substituída pela primeira. '''

s = input("Informe a string: ")
resultado = ""


for i in range(0, len(s)):
    resultado += s[i] + s[i+1]
    
print(resultado)
