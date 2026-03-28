# A Olimpíada Internacional de Informática (IOI, no original em inglês) é a mais prestigiosa competição de programação para alunos até o
#ensino médio; a cada ano, aproximadamente 300 competidores, de oitenta países, se reúnem em um país diferente para as provas da
#competição. Naturalmente, os competidores usam o tempo livre para acessar a Internet, programar e jogar em seus notebooks. No
#entanto, eles se depararam com um problema: o saguão do hotel só tem uma tomada. Felizmente, os quatro competidores da equipe
#brasileira da IOI trouxeram cada um uma régua de tomadas, permitindo assim ligar vários notebooks em uma só tomada do saguão.
#Eles sabem também que podem ligar uma régua em outra para aumentar ainda mais o número de tomadas disponíveis. No entanto,
#como as réguas têm muitas tomadas, eles pediram para você fazer um programa que, dado o número de tomadas em cada régua,
#determine o número máximo de notebooks que podem ser conectados num mesmo instante.
#○ Entrada: Ler quatro números inteiros positivos T1, T2, T3, T4, indicando o número de tomadas de cada uma das quatro réguas.
#○ Saída: Seu programa deve informar um único número inteiro, indicando o número máximo de notebooks que podem ser
#conectados a tomadas num mesmo instante

t1 = float (input("Informe o numero de tomadas da regua 1: "))
t2 = float (input("Informe o numero de tomadas da regua 2: "))
t3 = float (input("Informe o numero de tomadas da regua 3: "))
t4 = float (input("Informe o numero de tomadas da regua 4: "))

max = (t1 + t2 + t3 + t4) - 3

print (max)
