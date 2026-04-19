'''16. Crie um programa que identifique o maior palíndromo possível dentro de uma string. Exemplo: "abacdfgdcaba" →
"aba"'''

s = input("Digite a string: ")

maior = ""

# percorre início da substring
for i in range(len(s)):
    # percorre fim da substring
    for j in range(i, len(s)):
        
        # verifica se s[i:j+1] é palíndromo
        eh_palindromo = True
        
        inicio = i
        fim = j
        
        while inicio < fim:
            if s[inicio] != s[fim]:
                eh_palindromo = False
            inicio += 1
            fim -= 1
        
        # se for palíndromo e maior que o atual
        if eh_palindromo:
            tamanho_atual = j - i + 1
            tamanho_maior = len(maior)
            
            if tamanho_atual > tamanho_maior:
                maior = ""
                for k in range(i, j + 1):
                    maior += s[k]

print("Maior palíndromo:", maior)
