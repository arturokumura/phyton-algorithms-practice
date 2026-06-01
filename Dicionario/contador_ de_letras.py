IGNORE = " .,;:\t\n"
letra = {}
def main():
    frase = input("Digite uma frase: ")
    for c in frase:
        if c not in IGNORE:
            if c not in IGNORE:
                if c in letra:
                    letra[c] += 1
                else:
                    letra[c] = 1
    print(letra)
    keylist = list(letra.keys())
    keylist.sort()
    for i in keylist:
        print(i ,":", letra[i])
main()
