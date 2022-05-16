#操作列表
cars=['dongfeng','yiqi','beiqi','hongqi']
#for循环后面需要加上冒号:代表循环的开始
for car in cars: #for循环列表中的元素
    print(car)
    print(car.title() + " is very good!") #for循环下缩进显示
print(car.title() + " is very good!")#未缩进显示列表终值
print("all cars is perfect!") #结束循环最后输出

#小练习
pets=['cat','pig','snake','dog']
for pet in pets:
    print("A "+pet+" would make great pet!")
print("Any of these animals would make a great pet!")

##创建数值列表
#使用range()函数
for value in range(1,5):
    print(value)

numbers = list(range(1,10)) #list()函数变成列表
print(numbers)

even_numbers=list(range(1,11,3))#以1开始每一个加上3限制长度
print(even_numbers)
#1到100相加
list=[]
sum=0
for i in range(1,101):
    sum=sum+i
    list.append(sum)
print(sum)
print(list) #1到100每一个相连的相加直到加到100

##列表解析
numbers=[value**2 for value in range(1,10)]
print(numbers)

#小练习
list=[]
sum=0
for i in range(1,1001):
    list.append(i)
    sum=sum+i
print(max(list))
print(min(list))
print(list)
print(sum)
##
number=[]
for value in range(3,31):
    value_1=value%3
    if value_1 in range(3,31) and value in range(3,31):
        number.append(value)
        print(number)
    else:
        print(number)


