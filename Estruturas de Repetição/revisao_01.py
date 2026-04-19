'''Faça um algoritmo que receba dez idades, pesos e altura, calcule e mostre:
a. a média das idades das dez pessoas;
b. a quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50 m;
c. a percentagem de pessoas com idade entre 10 e 30 anos e que medem mais de 1,90 m ou
menos de 1,50 m.
'''
n = 0
total_idade = 0
condicao_b = 0
pessoas_condicao = 0
condicao_c = 0
print("------------------DADOS--------------------")
while n < 10:
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    print("----------------------------------")
    total_idade += idade

    if peso > 90 and altura < 1.50:
        condicao_b += 1
    if idade > 10 and idade < 30 and (altura > 1.90 or altura < 1.50):
        pessoas_condicao += 1
        
    n += 1
media_idade = total_idade / 10
condicao_c = (pessoas_condicao * 10) * 100
print(f"Média das idades: {media_idade}")
print(f"Pessoas com peso superior a 90 quilos e altura inferior a 1,50 m: {condicao_b}")
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos e que medem mais de 1,90 m ou menos de 1.50m: {condicao_c}%")
