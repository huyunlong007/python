##在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra', 'cheese'],  # 在字典中嵌套列表
}
print("you order a "+pizza['crust']+"- crust pizza "+"with the following topping:")
for topping in pizza['toppings']: #循环打印配料
    print("\t"+topping)
##
favorite_language = {
    'tony': ['python', 'C++'],
    'jerry': ['java', 'JS', 'C'],
    'tom': ['C#', 'C++'],
}
for name,languages in favorite_language.items():
    if len(languages) > 2:
        print(languages)
    for language in languages:
        print(language)
    if language == 'C++':
        print(name.title())
    else:
        print(str(len(favorite_language[name])))
print(max(str(len(favorite_language[name]))))

##在字典存储字典
users = {
    'ae': {
        'dragon': 'shanghai',
        'iqiq': 'haerbin',
    },
    'mc': {
        'xiaoyun': 'beijing',
        'xiaoqi': 'shenzhen',
    },
}
for user in users:
    print(user)
    for person,location in users[user].items(): #在字典下取值
        #print(person)
        print(person+": "+location)
    print("===========")

