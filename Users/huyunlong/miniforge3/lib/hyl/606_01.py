##
import json
filename = 'usernames.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what's your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you when you come back, " + username + "!")
else:
    print("welcome back,"+username+"!")

##重构
import json
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("what's your name?")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("we'll remember you when you come back, " + username + "!")
    else:
        print("welcome back," + username + "!")
greet_user()





























