def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("Como", "Cómo", "Qué", "Que", "Cuándo", "Cuando", "Donde", "Dónde", "Por qué", "Por que")
    if phrase.startswith(interrogatives):
        return "{}? ".format(capitalized)
    else:
        return "{}. ".format(capitalized)

aux = ""

while True:
    frase = input("Decime Algo: ").capitalize()
    if frase != "/end":
         aux = aux + sentence_maker(frase) 
         continue
    else:
        print(aux)
        break

