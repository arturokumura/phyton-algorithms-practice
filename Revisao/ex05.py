'''. Receba uma string e remova todas as letras consecutivas repetidas, mantendo apenas a primeira ocorrência de cada
sequência.'''

s = input("Informe a String: ")
res = ""

for i in range(len(s)):
    if i == 0:
        res += s[i]  # sempre pega o primeiro
    else:
        if s[i] != s[i-1]:
            res += s[i]

print(res)
