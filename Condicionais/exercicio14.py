#● Rosy é uma talentosa professora do Ensino Médio que já ganhou
#muitos prêmios pela qualidade de sua aula. Seu reconhecimento foi
#tamanho que foi convidada a dar aulas em uma escola da Inglaterra.
#Tudo ocorreu bem para Rosy até o dia da prova. Acostumada a dar
#notas de 0 (zero) a 100 (cem), ela fez o mesmo na primeira prova dos
#alunos da Inglaterra. No entanto, os alunos acharam estranho, pois
#na Inglaterra o sistema de notas é diferente: as notas devem ser
#dadas como conceitos de A a E. O conceito A é o mais alto, enquanto
#o conceito E é o mais baixo. Conversando com outros professores,
#ela recebeu a sugestão de utilizar a tabela ao lado, relacionando as
#notas numéricas com as notas de conceitos
#● Escreva um programa que recebe uma nota no sistema numérico e
#determina o conceito correspondente.

nota = float(input("Informe a nota do aluno: "))

if(nota == 0):
    print("E")
elif(nota > 0 and nota <= 35):
    print("D")
elif(nota >= 36 and nota <=60):
    print("C")
elif(nota >=61 and nota<=85):
    print("B")
else:
    print("A")
