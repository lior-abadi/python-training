import json
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def dictionary(w: str):

    w = w.lower()
    if (w not in data):
        return "Word not found"

    return data[w]

word  = input("Enter word: ")

print(dictionary(word))