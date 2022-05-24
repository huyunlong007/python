#返回字典
def build_person(first_name, last_name, age):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('h', 'dragon', 23)
print(musician)

##结合函数和whlie循环
'''
def get_formatted_name(first_name, last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nplease enter your name:")
    print("enter 'q' to quit at any time")
    f_name = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("hello, "+formatted_name)
'''
#小练习
def make_album(singer, song):
    song_message = singer+' '+song
    return song_message.title()
while True:
    print("\nplease tell me your favorite singer? and its song")
    print("would you like to want another respone?(yes/no)")
    fv_singer = input("singer: ")
    if fv_singer == 'no':
        break
    fv_song = input("song: ")
    if fv_song == 'no':
        break
    message = make_album(fv_singer, fv_song)
    print(message)
#
def make_album(singer, song):
    bulid_message = {'singer': singer, 'song': song}
    return bulid_message  #返回存储的参数
message = make_album("jay zhoou", "qintian")
print(message)

###传递列表



