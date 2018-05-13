#random notes while I was working through the project.
import json
# from pprint import pprint
import difflib
from difflib import SequenceMatacher[]
SequenceMatcher(None,"rainn", "rain")#First argement is junk meaning it ignores spaces
                                                                #and random characters that are not letters aka that is junk.
#returns <difflib.SequenceMatcher object at 0x10246fe80> which is a sequence matcher object which is nothing interesting.
SequenceMatcher(None,"rainn", "rain").ratio()#Need to apply the ratio method to get the actual ratio.
                                                                #ratio out put is 0.8888888888888888 this number indicate a singularity between
                                                                #these two strings on a scale from 0.00 to 1.00.
from difflib import get_close_matches[]
help(get_close_matches[])
        #get_close_matches(word, possibilites, n=3, cuttoff = 0.6) #===> word: the word you are trying to match
                                                                                                    #===> possibilities: the list of words to compare the word to
                                                                                                     #===> n =3: the amount of worlds to grab if any
                                                                                                     #===>cuttoff: the lost possible ratio score to consider
get_close_matches("rain", data.keys() , n=3, cuttoff = 0.6)
get_close_matches("rain", data.keys() )[0] # if you only want that word. Gives you only the first one.

with open('data.json') as f:
    data =json.load(f)
    # print(type(data)) #will print out the class of the type of data which is a dictionary.
    # print(data.keys())
    # print(data['rain'])
def  diction_ary(a) :
    a = a.lower()
    if  a in data:
        return (data[a])
    else:
        return ("does not exist in the enlgish lang. ")
user_input = input("Give me a word to look up!:\n")
# user_input =user_input.lower()
print(diction_ary(user_input))

#*******************************************************************************
#difflib — Helpers for computing deltas-
#************Attempting to grab the term aka the key with the value. **************
# search_by_key = input("Provide definition:\n")
# for diction in data.values():
#     if diction == search_by_key:
#         term= dictionary[diction]
#         print(term)
#     else:
#         return ("You suck!")

# print(len(data))
