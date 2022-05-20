#函数input()
name = input("please enter your name: ")
print("hello, "+name)
#
birthday_wish = "enter your name: "
name = input(birthday_wish)
print("happy birthday!"+name)

age = input("enter your age")
age = int(age) #把字符串转换成数值
if age >= 18:
   print(age)
#求模运算符
number = input("enter a number: ")
number = int(number)
if number % 3 == 0:
   print("this number "+str(number)+" is a even!")
else:
   print("this number "+str(number)+" is a odd!")








