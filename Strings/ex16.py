'''● Dado duas strings A e B, faça um programa que imprima “Sim” se A e B são
anagramas e “Nao”, caso contrário.
○ Anagrama: transposição de letras de palavra ou frase para formar outra palavra ou frase
diferente. Por exemplo: “roma” e “amor” são anagrama
● Considere como entrada apenas palavras com letras minúsculas
'''

A = input("Digite a primeira palavra: ")
B = input("Digite a segunda palavra: ")

if len(A) != len(B):
    print("Nao")
else:
    for i in range(len(A)):
        letra = A[i]
        
        contA = 0
        contB = 0

        # conta em A
        for j in range(len(A)):
            if A[j] == letra:
                contA += 1

        # conta em B
        for j in range(len(B)):
            if B[j] == letra:
                contB += 1

        if contA != contB:
            print("Nao")
            break
    else:
        print("Sim")
