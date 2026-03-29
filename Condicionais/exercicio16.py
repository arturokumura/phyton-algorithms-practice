A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))
C = int(input("Informe o valor de C: "))

# Ordenando
if A > B:
    A, B = B, A

if A > C:
    A, C = C, A

if B > C:
    B, C = C, B

print(f"Ordem crescente: A={A}, B={B}, C={C}")
