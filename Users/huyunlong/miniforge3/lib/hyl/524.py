#小练习
''''
favourite_resort = {}
while True:
    name = input("what's your name?")
    resort = input("If you could visit one place in the world, where would you go?")
    favourite_resort[name] = resort
    repeat = input("would you like want to another person reponse?(yes/no)")
    if repeat == 'no':
        break
print("\n------the following report------")
for name, resort in favourite_resort.items():
    print(name+",could visit "+resort+" in the world,do you like it?")
'''
#
