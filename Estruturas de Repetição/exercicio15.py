#Uma universidade deseja fazer um levantamento a respeito do seu concurso vestibular. Para
#cada curso, é fornecido o seguinte conjunto de valores: o código do curso; o número de vagas;
#número de candidatos do sexo masculino; número de candidatos do sexo feminino;
 #O último conjunto, para indicar fim de dados, contém o código do curso igual a zero.
 #Fazer um algoritmo que calcule escreva, para cada curso:
#a) o número de candidatos por vaga e a porcentagem de candidatos do sexo feminino
#(escreva também o código correspondente do curso);
#b) determine o maior número de candidatos por vaga e escreva esse número
#juntamente com o código do curso correspondente (supor que não haja empate);
#c) calcule e escreva o total de candidatos

maior = 0
cursomaior = 0
total_geral = 0

cod = int(input("Código do curso (0 para parar): "))

while(cod != 0):
   vagas = int(input("Número de vagas: "))
   masc = int(input("Candidatos do sexo masculino: "))
   fem = int(input("Candidatos do sexo feminino: "))
   print("-----------------------------------------")
   
   total = masc + fem
   total_geral += total
   cv = total / vagas
   pfem = (fem / total) * 100
   print(f"Número de candidatos por vaga: {cv}")
   print(f"Porcentagem de candidatos do sexo feminino: {pfem}, {cod}")

   if (cv > maior):
     maior = cv
     cursomaior = cod

   cod = int(input("Código do curso (0 para parar): "))



print(f"Maior número de candidatos por vaga: {maior}")
print(f"Curso com maior número de candidatos por vaga: {cursomaior}")
print(f"Total de candidatos: {total_geral}")
   
