R = float(input("Melhor resultado obtido por um atleta numa prova das Olimpíadas: "))
M = float(input("Recorde mundial: "))
L = float(input("Recorde olímpico: "))

if(R < M ):
    resultado1 = "RM"
else:
    resultado1 = '*'

if(R < L):
    resultado2 = "RO"
else:
    resultado2 = '*'

print(resultado1)
print(resultado2)
