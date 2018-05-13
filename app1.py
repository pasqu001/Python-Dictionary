import json
# import difflib
# import keyword
# from difflib import SequenceMatcher
from difflib import get_close_matches
# get_close_matches("rain", data.keys() , n=3, cuttoff = 0.6)
# get_close_matches("rain", data.keys() )[0]

with open('data.json') as f:
    data = json.load(f)

    def diction_ary(a):
        a = a.lower()
        if a in data:
            return (data[a])
        elif a.title() in data: #if user entered "texas" this will check for "Texas" as well.
            return data[a.title()]
        elif len(get_close_matches(a, data.keys())) > 0:
            yn = input("Did you mean %s instead? Type y for yes and n for no:\n" % get_close_matches(a, data.keys())[0])
            if yn == 'y':
                return (data[get_close_matches(a, data.keys())[0]])
            elif yn == 'n':
                return "Sorry we could not look up your word."
            else:
                return "We could not understand your input."
        else:
            return "Sorry I could not find that world. "

user_input = input("Give me a word to look up!:\n")

output = (diction_ary(user_input))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
