

opcao = input("Digite a, b ou c: ")

# -------- a --------
if opcao == "a":
    soma = 0
    den = 1
    for num in range(1, 100, 2):
        termo = num / den
        print(num, "/", den)
        soma = soma + termo
        den = den + 1
    print("Soma =", soma)


# -------- b --------
elif opcao == "b":
    soma = 0
    d = 50
    
    for i in range (1, 51):
        termo = (2 ** i) / d
        print (f"2 ** {i} /{d}")
        soma += termo
        d = d - 1
    print("Soma =", soma)


# -------- c --------
elif opcao == "c":
    soma = 0
    
    for i in range(1, 11, 1):
        termo = i / (i * i)  # i²

        if i % 2 == 0:
            soma = soma - termo
        else:
            soma = soma + termo
        
    print("Soma = ", soma)

else:
    print("errado")
