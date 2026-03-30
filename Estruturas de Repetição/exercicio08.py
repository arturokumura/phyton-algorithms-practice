N = int(input("Informe um número: "))

H= 0

for i in range(1, N + 1):
    H = H + (1 / i)
print(f"O número harmonico de H{N} é {H}")
