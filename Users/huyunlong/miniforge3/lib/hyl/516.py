#if 语句
cars=['audi','bmw','benz','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#if-elif-else
age = 123
if age < 4:
    print("your admission is $0.")
elif age < 18:
    print("your admission is $8.")
else:
    print("your admission is $10.")

#小练习
alien_colors = ['green','yellow','red']
for alien_color in alien_colors:
      if alien_color == 'green':
          print("players get 5 points.")
      elif alien_color != "red":
          print("players get 10 points.")
      else:
          print("thank you,please try again!")

#使用if语句处理列表
requestd_toppings = []
requestd_toppings.append("apple")
if requestd_toppings:     #判断是否需要元素
    for requestd_topping in requestd_toppings:
        print("adding "+requestd_topping+".")
    print("finished making your mizza!")
else:
    print("are you sure you want a plain pizza!")

#多个列表
cars = ['audi','bmw','benz']
super_cars = ['ferrari','lamborghini','bugatti','bmw','benz']
for car in cars:
    if car in super_cars:
        print("this super car is "+car)
    else:
        print("my favourite car is "+car)
