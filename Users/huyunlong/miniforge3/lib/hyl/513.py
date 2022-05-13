#使用列表中一部分元素--切片
fruits=['apple','banana','pear','mango','patota']
print(fruits[1:4]) #第二到四元素
print(fruits[0:4]) #第一到四元素
print(fruits[4:]) #第四元素后面到末尾
print(fruits[:4]) #开始到四元素
print(fruits[-2:]) #最后俩元素
print("my favourite fruit is ")
for fruit in fruits[3:]: #遍历切片元素
    print(fruit.title())

#小练习
socres=[89,23,46,78,98,100,35,38]
for score in socres[-3:]:
    print(score)

#
my_food=['pizza','beef','cake']
my_friend_food=my_food[-2:] #把切片赋给；不是把全部赋给
my_food.append('connoli')
my_friend_food.append('ice cream')
print("my favorite food is ")
print(my_food)
print("my friend favorite food is ")
print(my_friend_food)

#元组
orders=('noodle','soop','fruit')
for order in orders:
    print(order)
change_orders=('beef','banana') #不能修改元组里的元素，可以重新定义个元组
for change_order in change_orders:
    print(change_order)