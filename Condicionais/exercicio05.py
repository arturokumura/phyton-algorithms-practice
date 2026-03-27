nome = (input("Informe o nome do aluno: "))
nota1 = float(input("Informe nota 1: "))
nota2 = float(input("Informe nota 2: "))
nota3 = float(input("Informe nota 3: "))

peso1 = 1
peso2 = 2
peso3 = 3

media = (peso1 * nota1 + peso2 * nota2 + peso3 * nota3) / (peso1 + peso2 + peso3)

print (f"A média ponderada de {nome} é : {media} ")
