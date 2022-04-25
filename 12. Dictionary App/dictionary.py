import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(w: str):
    w = w.lower()
    resArray = get_close_matches(w, data.keys(), cutoff = 0.8)

    # Evaluate direct matches
    if w in data:
        return (data[w])
    elif w.title() in data:
        return (data[w.title()])
    elif w.upper() in data:
        return (data[w.upper()])
    
    # Evaluate word matches and mismatch.
    if (len(resArray) > 0):
        response = input(f"Did you mean instead {resArray[0]}, [Y/n]")
        if response.lower() == "y":
            return data[resArray[0]]
        else: 
            return "Your query was not properly understood. Try another word."
    else:
        return "Word not found"

word  = input("Enter word: ")
output = dictionary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)