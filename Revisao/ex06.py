'''Reorganize os caracteres de uma string de modo que todos os caracteres que estavam originalmente em índices
pares apareçam antes dos que estavam em índices ímpares.'''

s = input("Informe a String: ")
pares = ""
impares = ""
res: ""
for i in range(len(s)):
    if i % 2 == 0:
        pares += s[i]
    else:
        impares += s[i]
res = pares + impares
print(res)
