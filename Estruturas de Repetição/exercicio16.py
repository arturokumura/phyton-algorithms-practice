# -----------------------------------------------------------
# PROBLEMA: Cálculo de salários e estatísticas de operários
# -----------------------------------------------------------
#
# Em uma fábrica existem operários divididos em 3 classes:
#
# Classe A: até 30 peças por mês
# → recebe apenas o salário mínimo
#
# Classe B: de 31 a 35 peças
# → salário mínimo + 3% do salário mínimo por peça acima de 30
#
# Classe C: mais de 35 peças
# → salário mínimo + 5% do salário mínimo por peça acima de 30
#
# -----------------------------------------------------------
# ENTRADAS:
# - Número do operário (0 encerra o programa)
# - Quantidade de peças produzidas no mês
# - Sexo do operário (M ou F)
#
# -----------------------------------------------------------
# SAÍDAS:
# - Salário de cada operário
# - Total da folha de pagamento
# - Total de peças produzidas
# - Média de peças dos homens por classe (A, B, C)
# - Média de peças das mulheres por classe (A, B, C)
# - Número do operário com maior salário (sem empate)
#
# -----------------------------------------------------------

salario_minimo = 1621
homens = 0
mulheres = 0
pecas_total = 0
maior_salario = 0
num_maior = 0
folha = 0

print("---------Informações do operário---------")
num = int(input("Número do operário (0 para parar): "))
while(num != 0):
    pecas = int(input("Peças fabricadas por mês: "))
    sexo = (input("Sexo (M/F): "))

    if(pecas <= 30):
        classe = "A"
        salario = salario_minimo
    elif(pecas <=35):
        extra = pecas - 30
        salario = salario_minimo + (extra *(salario_minimo * 0.03))
        classe = "B"
    else:
        extra = pecas - 30
        salario = salario_minimo + (extra *(salario_minimo * 0.05))
        classe = "C"

    pecas_total += pecas
    if(sexo == 'M'):
        homens += 1
    else:
        mulheres += 1

    
    folha += salario

    if(salario > maior_salario):
        maior_salario = salario
        num_maior = num

    print(f"Salário do operário {num}: {salario}")
      # Próximo operário
    num = int(input("Número do operário (0 para parar): "))

if(homens > 0):
    media_m = pecas_total / homens
else:
    media_m = 0

if(mulheres > 0):
    media_f = pecas_total / mulheres
else:
    media_f = 0

print("\n---------RESULTADOS---------")
print(f"Folha mensal de pagamento da fábrica: {folha}")
print(f"Média de peças fabricadas por homens na classe {classe}: {media_m}")
print(f"Média de peças fabricadas por mulheres na classe {classe}: {media_f}")
print(f"Número do operário de maior salário: {num_maior}")
