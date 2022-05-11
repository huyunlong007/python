#列表;提取列表元素
super_car=['ferrari','lamborghini','bugatti']
message='my first dream car is'
print(super_car)
print(super_car[1])
print(super_car[0].title())
print(super_car[2].upper())
print(super_car[-1].title())
print(message+"\t"+super_car[0].title()+"!")

#修改、删除元素
motorcycle=['honda','yamaha','suzuki']
#print(motorcycle)
motorcycle[-1]='ducati'
#print(motorcycle)
motorcycle.append('bmw') #在末尾添加元素
print(motorcycle)
motorcycle.insert(1,'linmu') #添加元素
print(motorcycle)
del motorcycle[1] #del删除元素,后面不再使用该元素
print(motorcycle)

poped_motorcycle=motorcycle.pop() #pop删除末尾元素，并能接着使用
print(motorcycle)
print(poped_motorcycle)
motorcycle.remove('yamaha') #删除对应元素还可以使用
print(motorcycle)
too_expensive='ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print("\na "+too_expensive+"\tis too expensive for me !")

#组织列表
cars=['BMW','bugatti','audi','lamburghini','Ferrgri']
cars.sort() #sort()按字母顺序排列
print(cars)



