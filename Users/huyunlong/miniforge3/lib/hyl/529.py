##访问属性
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describle_restaurant(self):
        print("this "+self.cuisine_type+"'s restaurant's name is "+self.restaurant_name)
    def open_restaurant(self):
        print("the restaurant is opening!")

class Restaurant():
    my_restaurant = Restaurant("KFC", "24-h")
    print("my restaurant'name is "+my_restaurant.restaurant_name)
    print("my restaurant's cuisine_type is "+my_restaurant.cuisine_type)

    my_restaurant = Restaurant("M", "fast-lunch")
    my_restaurant.describle_restaurant()

##小练习
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name +" "+ last_name
    def describe_user(self):
        print("this user's name is "+self.first_name.title()+" "+self.last_name.title())
    def greet_user(self):
        print("hello,"+self.full_name.title()+"!")

class User():
    user = User('h', 'dragon')
    print("user's name is "+user.full_name)
    user = User('fan', 'qi')
    user.describe_user()
    user.greet_user()

#使用类和实例










