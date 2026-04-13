'''2. Dada uma string de entrada, substitua todas as ocorrências da primeira letra pela segunda, todas da segunda pela
terceira, e assim por diante até a última ser substituída pela primeira.'''

s = input("Informe a String: ")

if len(s) > 1:
    resultado = s[1:] + s[0]
else:
    resultado = s 

print("Resultado:", resultado)
print(s)
