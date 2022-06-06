##
import json
filename = 'usernames.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what's your name?")
    with open(filename, 'w') as f_obj:
        json.dump(filename, f_obj)
        print("we'll remember you when you come back, " + username + "!")
else:
    print("welcome back,"+username+"!")