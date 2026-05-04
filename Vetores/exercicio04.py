'''4. Faça um programa que construa duas listas A e B de 5 elementos cada. Após isso
leia 10 valores e adicione os 5 primeiros na lista A e os 5 últimos na lista B. Crie uma
terceira lista C, composta pela soma dos elementos de A e B que se encontram em
posições correspondentes. Após isso, escreva o conteúdo das listas A, B e C, com
elementos separados por vírgula'''
A = []
B = []
C = []
for i in range(5):
    va = float(input("Informe um valor para o vetor A: "))
    A.append(va)
    
for m in range(5):
    vb = float(input("Informe um valor para o vetor B: "))
    B.append(vb)
    
for j in range(10):
    if j <= 4:
        n = float(input("Informe um valor: "))
        A.append(n)
    else:
        n = float(input("Informe um valor: "))
        B.append(n)
#Soma
num = 0
for i in range(len(A)):
    num = A[i] + B[i]
    C.append(num)
print(f"Lista A: {A}")
print(f"Lista B: {B}")
print(f"Lista C: {C}")

