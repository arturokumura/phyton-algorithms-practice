from ex01 import *

print("Testando ValidaInteiroPositivo")
print(ValidaInteiroPositivo("123"))
print(ValidaInteiroPositivo("+456"))
print(ValidaInteiroPositivo("-789"))

print("\nTestando ValidaInteiro")
print(ValidaInteiro("123"))
print(ValidaInteiro("-456"))
print(ValidaInteiro("+789"))
print(ValidaInteiro("12.3"))

print("\nTestando NumeroReal")
print(NumeroReal("12.5"))
print(NumeroReal("-7.8"))
print(NumeroReal("+3.14"))
print(NumeroReal("123"))
print(NumeroReal("1.2.3"))
