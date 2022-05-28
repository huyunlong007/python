####类
###创建和使用类
class Dog():  #定义一个Dog的类，在python中首字母大写的名称指的是类
    def __init__(self, name, age):  #方法_init_()类中的函数成为方法
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")

class Dog():
    my_dog = Dog('sinba', 7)  #创建一个实例
    print("my dog's name is "+my_dog.name.title())
    print("my dog is "+str(my_dog.age)+" years old")
