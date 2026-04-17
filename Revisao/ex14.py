'''14. Implemente um algoritmo que dada uma string retorne uma quantidade de vezes que cada substring contígua de
tamanho 3 aparece no texto. Exemplo: "abcaabcabc" Saída: abc: 3 bca: 2 caa: 1 aab: 1 cab: 1 '''
s = input("Digite a frase: ")
contadas = ""

for i in range(len(s) - 2):
    sub = s[i:i+3]
    
    if sub not in contadas:
        cont = 0
        
        for j in range(len(s) - 2):
            if s[j:j+3] == sub:
                cont += 1
        
        print(sub, ":", cont)
        contadas += sub
