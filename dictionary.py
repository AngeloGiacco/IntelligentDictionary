import json
from difflib import get_close_matches
data = json.load(open("data.json"))
for x in data.keys():
    x = x.lower()
query = input("What would you like to find the meaning of?").lower()
if query in data:
    for definition in data[query]:
        print(definition)
elif query.title() in data:
    for definition in data[query.title()]:
        print(definition)
elif query.upper() in data:
    for definition in data[query.upper()]:
        print(definition)
elif len(get_close_matches(query, data.keys(), cutoff = 0.8)) > 0:
    match = get_close_matches(query, data.keys(), cutoff = 0.8)[0]
    acceptable = input("Did you mean "+match+" instead? Yes or no?").lower()
    if acceptable == "yes":
        for definition in data[match]:
            print(definition)
    else:
        print("There is no such word as your query, please double check it!")
else:
    print("There is no such word as your query, please double check it!")
#print(SequenceMatcher(None,"rain","rainn").ratio())
#extend following completion of course to a website
