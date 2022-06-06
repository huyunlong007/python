##
import json
def get_stored_username():  #存储了用户名就获取
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    username = get_stored_username()
    if username:
        print("welcome back," + username + "!")
    else:
        username = input("what's your name?")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("we'll remember you when you come back, " + username + "!")
greet_user()

##小练习
'''
import json
number = input("please enter your favorite number:")
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
'''
#
import json
filename = 'number.json'
with open(filename) as f_obj:
    number = json.load(f_obj)
    print(number)
##
import json
filename = 'number.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("please enter your favorite number:")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
else:
    print("your lucky number is "+number+" !")

##
import json
def get_stored_username():
    filename = 'username_2.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("what's your name?")
    filename = 'username_2.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_username():
    username = get_stored_username()
    if username:
        print("welcome back," + username + "!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, " + username + "!")
greet_username()










