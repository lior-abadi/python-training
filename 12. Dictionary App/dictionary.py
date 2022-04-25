import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(w: str):
    w = w.lower()
    resArray = get_close_matches(w, data.keys(), cutoff = 0.8)

    # Evaluate perfect match.
    if w in data:
        return (f"{w}: {data[w]}")

    # Evaluate word matches and mismatch.
    if (len(resArray) > 0):
        response = input(f"Did you mean instead {resArray[0]}, [Y/n]")
        if response.lower() == "y":
            return data[resArray[0]]
        else: 
            return "Okay, you can try another word."
    else:
        return "Word not found"

word  = input("Enter word: ")

print(dictionary(word))