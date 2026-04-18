'''15. Implemente um algoritmo que converta um número romano (como string) para um número inteiro. Exemplo:
"MCMXCIV" → 1994.'''

s = input("Digite o número romano: ")

total = 0

for i in range(len(s)):
    # valor atual
    if s[i] == 'I':
        atual = 1
    elif s[i] == 'V':
        atual = 5
    elif s[i] == 'X':
        atual = 10
    elif s[i] == 'L':
        atual = 50
    elif s[i] == 'C':
        atual = 100
    elif s[i] == 'D':
        atual = 500
    elif s[i] == 'M':
        atual = 1000

    # verifica o próximo (se existir)
    if i < len(s) - 1:
        if s[i+1] == 'I':
            prox = 1
        elif s[i+1] == 'V':
            prox = 5
        elif s[i+1] == 'X':
            prox = 10
        elif s[i+1] == 'L':
            prox = 50
        elif s[i+1] == 'C':
            prox = 100
        elif s[i+1] == 'D':
            prox = 500
        elif s[i+1] == 'M':
            prox = 1000

        if atual < prox:
            total = total - atual
        else:
            total = total + atual
    else:
        total = total + atual

print(total)
