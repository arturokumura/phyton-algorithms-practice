'''1. Cifra da Nlogônia
O rei da Nlogônia ordenou que todos os documentos importantes sejam "cifrados",
para que apenas quem tem conhecimento da cifra possa lê-los (cifrar um documento
significa alterar o original modificando as letras de acordo com algum algoritmo de
cifra).
O rei decretou que o seguinte algotimo deve ser usado para cifrar os documentos:
 Cada consoante deve ser substituída por exatamente três letras, na seguinte
ordem:
1. a própria consoante (vamos chamar de consoante original);
2. a vogal mais próxima da consoante original no alfabeto, com a regra
adicional de que se a consoante original está à mesma distância de duas
vogais, então a vogal mais próxima do início do alfabeto é usada. Por
exemplo, se a consoante original é d, a vogal que deve ser usada é e, pois
esta é a vogal mais próxima; se a consoante original é c, a vogal que deve
ser utilizada é a, porque c está à mesma distância de a e e, e a é mais
próxima do início do alfabeto.
3. a consoante que segue a consoante original, na ordem do início ao fim do
alfabeto. Por exemplo, se a consoante original é d, a consoante a ser
utilizada é f. No caso de a consoante original ser z, deve ser utilizada a
própria letra z.
 As vogais não são modificadas.
Nesta tarefa, o alfabeto é
a b c d e f g h i j k l m n o p q r s t u v x z
e as vogais são
a e i o u
Por exemplo, a cifra da palavra "ter" é "tuveros" (tuv-e-ros) e a cifra da palavra "paz" é
"poqazuz" (poq-a-zuz).
O rei da Nlogônia procura por alguém que saiba escrever um programa que produza a
cifra de uma palavra dada. Você pode ajudá-lo?'''

palavra = input("Digite a palavra: ")

vogais = "aeiou"
alfabeto = "abcdefghijklmnopqrstuvwxyz"

resultado = ""

for c in palavra:
    
    # verifica se é vogal
    eh_vogal = False
    for v in vogais:
        if c == v:
            eh_vogal = True
    
    if eh_vogal:
        resultado += c
    
    else:
        # 1. própria consoante
        resultado += c
        
        # 2. achar vogal mais próxima
        menor_dist = 100
        vogal_proxima = ""
        
        for v in vogais:
            # calcular posição de c
            pos_c = 0
            pos_v = 0
            
            i = 0
            for letra in alfabeto:
                if letra == c:
                    pos_c = i
                if letra == v:
                    pos_v = i
                i += 1
            
            # distância manual
            if pos_c > pos_v:
                dist = pos_c - pos_v
            else:
                dist = pos_v - pos_c
            
            if dist < menor_dist:
                menor_dist = dist
                vogal_proxima = v
        
        resultado += vogal_proxima
        
        # 3. próxima consoante
        if c == 'z':
            resultado += 'z'
        else:
            achou = False
            i = 0
            
            for letra in alfabeto:
                if letra == c:
                    achou = True
                elif achou:
                    # verifica se não é vogal
                    eh_vogal2 = False
                    for v in vogais:
                        if letra == v:
                            eh_vogal2 = True
                    
                    if not eh_vogal2:
                        resultado += letra
                        break

print(resultado)

