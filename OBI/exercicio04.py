A = float(input("Informe o ponto A: "))
B = float(input("Informe o ponto B: "))
C = float(input("Informe o ponto C: "))

if ((B - A) < ( C - B)):
    print("1")
elif ((B - A) > (C - B)):
    print("-1")
else:
    print("0")

