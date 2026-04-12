N = int(input("Quantos caracteres tem a primeira palavra?: "))
p = input("Digite a primeira palavra: ")
M = int(input("Quantos caracteres tem a segunda palavra?: "))
s = input("Digite a segunda palavra: ")
cont = 0
for i in range(N):
    for j in range(M):
        if p[i] == s[i]:
            cont+=1
            break
        else:
            print("0")
print(cont)
    
