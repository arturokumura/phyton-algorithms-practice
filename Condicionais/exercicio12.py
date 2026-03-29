quantidade = float (input("Informe a quantidade de livros: "))

A = 7.5 + (0.25 * quantidade)
B = 2.5 + (0.50 * quantidade)

print(f"Valor com critério de pagamento A: {A}")
print(f"Valor com critério de pagamento B: {B}")

if(A < B):
    print(f"O critério de pagamento A é mais vantajoso")
else:
    print(f"O critério de pagamento B é mais vantajoso")
