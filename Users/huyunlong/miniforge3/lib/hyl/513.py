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