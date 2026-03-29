valor = float(input("Digite o valor da compra: R$ "))

if valor <= 100:
    desconto = valor * 0.05
elif valor < 200:
    desconto = valor * 0.10
else:
    desconto = valor * 0.20

total = valor - desconto

print(f"Desconto: R$ {desconto} ")
print(f"Total a pagar: R$ {total}")
