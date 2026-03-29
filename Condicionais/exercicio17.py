idade = float(input("Informe a idade: "))

if(idade > 65):
    print("Dispensado")
elif(idade >= 18 and idade <= 65):
    print("Obrigatório")
elif(idade >= 16 and idade <= 17):
    print("Facultativo")
else:
    print("Não pode votar")
