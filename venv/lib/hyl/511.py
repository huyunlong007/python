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
del motorcycle[1] #删除元素
print(motorcycle)

