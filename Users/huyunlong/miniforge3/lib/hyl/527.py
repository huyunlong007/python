#禁止修改函数列表
def print_models(unprinted_designs, completed_models):  #定义一个print_model函数
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model:"+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nthe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

#小练习
def show_magicians(names):
    for name in names:
        print("\nthis magician's name is "+name.title())
usernames = ['jay zhou', 'jack chen']
show_magicians(usernames)

##
def show_magicians(names, greats):
    while names:
        name = names.pop()
        print("the magician's name is "+name.title())
        greats.append(name)
def make_great(greats):
    print("\nthe following modifying name is: ")
    for great in greats:
        print("the great "+great)  #在每个名字加入the great
names = ['hyl', 'xiaohu']
greats = []
show_magicians(names[:], greats)  #保留原列表信息
make_great(greats)

##传递任意数量的实参
def make_pizza(size, *toppings):  #定义一个topping空元组
    print(size)
    print(toppings)
    '''
    for topping in toppings:
        print(topping)
    '''
make_pizza(16, 'pepperoni')
make_pizza(19, 'mushrooms', 'green peppers', 'extra cheese')

#
def make_pizza(size, *toppings):
    print("\nmaking a "+str(size)+"-inch pizza with the following toopings: ")
    for topping in toppings:
        print("- "+topping)
make_pizza(11, 'pepperoni')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

#使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): #遍历键值对
        profile[key] = value
    return profile
user_profile = build_profile('h', 'dragon', location = 'benjing' , filed = 'python')
print(user_profile)

#小练习
def make_car(manufacturer, type, **user_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['type'] = type
    for key, value in user_info.items():
        car[key] = value
    return car
message_car = make_car('BMW', 'BMW745', date = '2022-5-27', price = 100)
print(message_car)




























