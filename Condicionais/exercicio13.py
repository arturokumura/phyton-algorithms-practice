a = float (input("Informe o valor do coeficiente A: "))
b = float (input("Informe o valor do coeficiente B: "))
c = float (input("Informe o valor do coeficiente C: "))

delta = b**2 - 4 * a * c
x1 = (-b + delta** 0.5) / 2*a
x2 = (-b - delta** 0.5) / 2*a

if (delta < 0) :
    print("A equação não possui raízes reais")
else:
    print(f"As raízes da equação são: {x1} e {x2}")
