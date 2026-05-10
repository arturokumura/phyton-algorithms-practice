n = int(input("Números da sequência: "))
lista = []
maior = 1
for i in range(n):
    i = int(input())
    lista.append(i)

grupo = [lista[0]]
for i in range(1,len(lista)):
    if lista[i] != lista[i-1]:
        parar = False

        for elemento in grupo:
            if elemento == lista[i]:
                
                parar = True
        if not parar:
            grupo.append(lista[i])
    
if len(grupo) > maior :
    maior = len(grupo)
print(maior)
