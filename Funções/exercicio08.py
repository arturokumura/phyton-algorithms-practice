'''Faça uma função que recebe a data de nascimento (“dd/mm/aaaa”) e
retorna a string contendo a data com o mês por extenso. Exemplo: Data de
Nascimento: 29/10/1973  29 de Outubro de 1973.'''
def data(d):
    dia = d[0:2]
    mes = d[3:5]
    ano = d[6:]
    if mes == "01":
        mes = "Janeiro"
    elif mes == "02":
        mes = "Fevereiro"
    elif mes == "03":
        mes = "Março"
    elif mes == "04":
        mes = "Abril"
    elif mes == "05":
        mes = "Maio"
    elif mes == "06":
        mes = "Junho"
    elif mes == "07":
        mes = "Julho"
    elif mes == "08":
        mes = "Agosto"
    elif mes == "09":
        mes = "Setembro"
    elif mes == "10":
        mes = "Outubro"
    elif mes == "11":
        mes = "Novembro"
    elif mes == "12":
        mes = "Dezembro"
    return "Data de nascimento: "+ dia +" de " + mes +" de " + ano

print("--------Data de nascimento-------")
date = input("Digite a data de nascimento(dd/mm/aaaa): ")
print(data(date))
