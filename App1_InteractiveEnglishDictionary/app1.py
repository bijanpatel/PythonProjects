import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def fetchMeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn =  input("Did you mean {} ? Enter 'Y' for yes and 'N' for no.".format(get_close_matches(word,data.keys())[0]))
        if yn.upper() == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.upper() == 'N':
            return ("The word doesn't exist")
        else:
            return ("Invalid option")

    else:
        return ("The word doesn't exist")


w = input("Enter the Word::")
output = fetchMeaning(w)

if type(output) == list:
    for meaning in output:
        print(meaning)
else:
    print(output)


