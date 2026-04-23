'''Luiza está se preparando para começar a estudar em uma nova escola que será inaugurada na
avenida em que ela mora. A avenida possui 2,000 metros de comprimento e existe um ponto de
ônibus a cada 400 metros, incluindo no início e no m da avenida. A tabela abaixo indica a distância
de cada ponto de ônibus para o início da avenida.
Ponto
#1 Ponto #2 Ponto #3 Ponto #4 Ponto #5 Ponto #6
0 m 400 m 800 m 1200 m 1600 m 2000 m
A casa de Luiza está localizada no início da avenida, junto ao primeiro ponto de ônibus. A escola,
por outro lado, está localizada a uma distância D do início da avenida.
Luiza pretende pegar o ônibus na porta de casa, descer no ponto de ônibus mais próximo da escola
e andar a pé o restante do trajeto. Assim, por exemplo, se a escola está a uma distância D = 720 m
do início da avenida, ela vai descer no terceiro ponto de ônibus, localizado a 800 metros do início,
e andar 80 metros (em direção ao início da avenida) para chegar à escola.
Luiza pediu sua ajuda para descobrir quantos metros ela precisará andar: dada a distância em
metros D da escola para o início da avenida, determine qual a distância entre a escola e o ponto de
ônibus mais próximo.
Entrada
A entrada é composta por uma única linha contendo um único inteiro D, representando a distância
em metros da escola para o início da avenida.
Saída
Seu programa deverá imprimir uma única linha contendo um único inteiro, a distância mínima em
metros que Luiza precisará andar entre um ponto de ônibus e a escola.
Restrições
 0 ≤ D ≤ 2000
Informações sobre a pontuação
A tarefa vale 100 pontos. Estes pontos estão distribuídos em subtarefas, cada uma com suas
restrições adicionais às denidas acima.
 Subtarefa 1 (0 pontos): Esta subtarefa é composta apenas pelos exemplos mostrados
abaixo. Ela não vale pontos, serve apenas para que você verique se o seu programa imprime
o resultado correto para os exemplos.
 Subtarefa 2 (30 pontos): D < 800.
 Subtarefa 3 (70 pontos): Sem restrições adicionais.
Seu programa pode resolver corretamente todas ou algumas das subtarefas acima (elas não precisam
ser resolvidas em ordem). Sua pontuação nal na tarefa é a soma dos pontos de todas as subtarefas
resolvidas corretamente por qualquer uma das suas submissões.'''


d = int(input("Informe a distância D: "))

resto = d % 400

if resto < 400 - resto :
    resposta = resto
else:
    resposta  = 400 - resto
print(resposta)
