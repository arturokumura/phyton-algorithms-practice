'''Escreva uma função que recebe um número inteiro positivo entre 0 e 99 e
retorne a string contendo o número por extenso.'''
def numero(d):
    unidade = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = [ "dez", "onze", "doze", "treze", "quatorze","quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["","", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if d < 0 or d > 99:
        print("Número fora do intervalo")
    else:
        if d < 10:
            return unidade[d]
        elif d < 20:
            return especiais[d - 10]
        else:
            dezena = d // 10      
            u = d % 10      

        
            if u == 0:
                return dezenas[dezena]

            
            return dezenas[dezena] + " e " + unidade[u]

print("---------Número por extenso----------")
num = int(input("Informe um número: "))
print(numero(num))
