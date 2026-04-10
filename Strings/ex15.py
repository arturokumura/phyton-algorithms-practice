'''● Faça um programa que leia uma string e imprima “Sim” se é palíndromo e “Nao”,
caso contrário.
○ Palíndromo: diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a
direita ou vice-versa. Por exemplo: “arara” é um palíndromo
● Considere como entrada apenas palavras com letras minúsculas e sem espaços'''

str = input("Informe uma String para verificar se é palindromo ou não: ")
palindromo= ""

for i in range(len(str)-1 , -1, -1):
    palindromo += str[i]

#Verificar se é palíndromo ou não
if(palindromo == str):
    print(f"A string {str} é palíndromo")
else:
    print(f"A string {str} não é palíndromo")
