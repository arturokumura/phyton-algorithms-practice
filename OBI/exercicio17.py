'''3. Casamento de inteiros
Vamos definir a operação de casamento de dois números inteiros A e B da seguinte
forma:
 inicialmente fazemos A e B terem o mesmo número de dígitos, adicionando zeros
à esquerda conforme necessário;
 então cada dígito de A (do menos significativo ao mais significativo) é
comparado com o dígito correspondente de B, e o dígito de menor valor é
eliminado do número a que pertence (se os dígitos são iguais nenhum é
eliminado).
 o resultado da operação de casamento é o par de números inteiros formados
pelos dígitos remanescentes de A e B. No caso de não haver digito remanescente
para um dos números, o resultado para esse número é -1.
Por exemplo, considere o casamento de 69961 com 487920:
O resultado do casamento é o par de números 489 e 9961. Dados dois números inteiros,
sua tarefa é determinar o resultado do casamento desses dois números.
Entrada
A primeira linha da entrada contém um número inteiro A, a segunda linha contém um
número inteiro B.
Saída
Seu programa deve produzir uma única linha, contendo os dois números inteiros
produzidos pelo casamento dos números dados, em ordem não decrescente.'''
A = int(input("Digite A: "))
B = int(input("Digite B: "))
listaa = []
listab = []
lista_a = []
lista_b  = []
while A > 0:
    dig = A % 10
    listaa.append(dig)
    A = A // 10

for i in range(len(listaa)-1, -1, -1):
    lista_a.append(listaa[i])
    
while B > 0:
    dig = B % 10
    listab.append(dig)
    B = B // 10

for i in range(len(listab)-1, -1, -1):
    lista_b.append(listab[i])

res = []
if len(lista_a) == len(lista_b) :
    for i in range(len(lista_a)):
        if lista_a[i] > lista_b[i]:
            res.append(lista_a[i])
        else:
            res.append(lista_b[i])
    print(res)
else:
    
    nova_a = []
    nova_b = []
    if len(lista_a) > len(lista_b):
        tam = len(lista_a)
    else:
        tam = len(lista_b)
    for i in range(tam - len(lista_a)):
        nova_a.append(0)
    for elemento in lista_a:
        nova_a.append(elemento)

    for j in range(tam - len(lista_b)):
        nova_b.append(0)
    for elemento_b in lista_b:
        nova_b.append(elemento_b)

    resA = []
    resB = []

    for i in range(len(nova_a)):
       if nova_a[i] > nova_b[i]:
          resA.append(nova_a[i])
       elif nova_b[i] > nova_a[i]:
          resB.append(nova_b[i])
       else:
          resA.append(nova_a[i])
          resB.append(nova_b[i])
print(resB , resA)
