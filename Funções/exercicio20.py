'''Faça uma função que recebe duas strings e retorna True se as strings são anagrama
ou False caso contrário. Ex.:
roma, amor  True
ovo, vov  False'''
def anagrama(s1,s2):
    cont1 = 0
    cont2 = 0
    if len(s1) != len(s2):
        return False
    else:
        for c in s1:            
            #Conta A
            for i in range(len(s1)):
                if c == s1[i]:
                    cont1 += 1
            #ContaB
            for j in range(len(s2)):
                if c == s2[j]:
                    cont2 += 1
    if cont1 != cont2:
        return False
    else:
        return True

print("---------Anagrama---------")
frase1 = input("Digite a frase 1: ")
frase2 = input("Digite a frase 2: ")
print(anagrama(frase1,frase2))
