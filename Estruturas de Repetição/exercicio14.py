#● Faça um algoritmo que leia um número inteiro X. A partir dele tem-se um novo
#x de acordo com a seguinte regra
#○ se X é par, X = X / 2
#○ se X é impar, X = 3 * X + 1
#● O algoritmo deve escrever todos os valores até parar. A condição de parada é
#quando X tiver o valor final de 1.

x = int(input("Informe um numero x: "))

while x != 1:
    print(x)
    
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1

print(1)
