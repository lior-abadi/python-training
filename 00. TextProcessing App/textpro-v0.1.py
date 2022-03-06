text = input("Say Something: ")
aux = text.capitalize()

while True:
    text = input("Say Something: ")
    if text != "/end":
        aux = aux + ". " + text.capitalize()
        continue
    else:
        aux = aux + "."
        print(aux)
        break
