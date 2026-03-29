#● Uma determinada loja está fazendo promoções de vendas. Qualquer compra que
#um cliente fizer até R$ 100,00 receberá 5% de desconto. Se a compra for maior
#que R$ 100,00, mas inferior a R$ 200,00, o desconto será de 10%. Se for superior
#ou igual a R$ 200,00, o desconto será de 20%.
#● Faça um programa que calcule o desconto do total da compra de um cliente, e
#informe também, o total a pagar já com os descontos

valor = float(input("Digite o valor da compra: R$ "))

if valor <= 100:
    desconto = valor * 0.05
elif valor < 200:
    desconto = valor * 0.10
else:
    desconto = valor * 0.20

total = valor - desconto

print(f"Desconto: R$ {desconto}")
print(f"Total a pagar: R$ {total}")
