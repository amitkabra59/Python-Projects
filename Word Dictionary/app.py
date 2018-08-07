import json
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))


def dict_app(user_input):
    user_input = user_input.lower()
    if user_input in data:
        return data[user_input]
    elif user_input.title() in data:
        return data[user_input.title()]
    elif user_input.upper() in data:  # in case user enters words like USA or NATO
        return data[user_input.upper()]
    elif len(get_close_matches(user_input,data.keys()))>0:
         yn = input("Did you mean %s instead? Enter Y for yes and N for no: " % get_close_matches(user_input, data.keys(), cutoff= 0.8)[0]).lower()
         if yn == "y":
             return data[get_close_matches(user_input, data.keys(), cutoff=0.8)[0]]
         elif yn=="n":
             return "The word does no exists. Double check it!"
         else:
             return "We didn't understand your entry."
    else:
        return "The word does no exists. Double check it!"

user_input = input("Enter the word to search meaning!")


output = dict_app(user_input)

if type(output)== list:
    for item in output:
        print(item)

else:
    print(output)