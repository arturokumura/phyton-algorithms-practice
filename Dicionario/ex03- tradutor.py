dic_pirata = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "boy": "matey",
    "madam": "proud beauty",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "lawyer": "foul blaggart",
    "the": "th",
    "restroom": "head",
    "my": "me",
    "hello": "avast",
    "is": "be",
    "man": "matey"
}

def tradutor(frase):
    palavra = ""
    final = ""
    parar = False
    for c in frase:
        if c != " ":
            palavra += c
        else:
            final += dic_pirata.get(palavra,palavra)
            final += c
            palavra = ""
    final += dic_pirata.get(palavra,palavra)
    return final

Frase = input("Frase: ")
print(tradutor(Frase))
            
        
