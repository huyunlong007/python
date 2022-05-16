#if 语句
cars=['audi','bmw','benz','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#if-elif-else
age=123
if age<4:
    print("your admission is $0.")
elif age<18:
    print("your admission is $8.")
else:
    print("your admission is $10.")

#小练习
alien_colors=['green','yellow','red']
for alien_color in alien_colors:
      if alien_color=='green':
          print("players get 5 points.")
      elif alien_color !="red":
          print("players get 10 points.")
      else:
          print("thank you,please try again!")

#
