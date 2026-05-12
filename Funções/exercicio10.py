'''Faça uma função que recebe duas strings. Admita que elas terão o mesmo
número de caracteres. A função deve retornar uma string com as letras
intercaladas: Instituto, FederalSP  IFnesdteirtaultSoP'''
def inter(s1,s2):
    nova = ""
    if len(s1) != len(s2):
        return "As strings devem ter o mesmo tamanho"
    else:
        for i in range(len(s1)):
            nova += s1[i]
            nova += s2[i]
        return nova

print("---------Intercalar Strings----------")
str1 = input("Digite a primeira frase: ")
str2 = input("Digite a segunda frase: ")
print(inter(str1,str2))
