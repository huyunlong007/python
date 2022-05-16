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

####字典:一系列键-值对（key-value）
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("you earned "+str(new_points)+" points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 27
print(alien_0)

#
alien_0 = {} #创建空字典
alien_0['color'] = 'red'
alien_0['points'] = 28
print(alien_0)
print("this alien is "+alien_0['color'])
alien_0['color'] = 'black' #修改键值
print("this alien is now "+alien_0['color'])

##




