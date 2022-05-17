alien = {'x_position' :2,'y_position' :25,'speed': 'medium'}
print("original x_position: "+str(alien['x_position'])) #输出之前坐标
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'fast':
    x_increment = 3
else:
    x_increment = 2
alien['x_position'] = alien['x_position'] + x_increment
print("new x_position: "+str(alien['x_position'])) #输出变化后坐标
alien['points'] = 7  #添加一个键值
print(alien)
del alien['y_position']  #删除一个键值
print(alien)

##类似对象组成的字典
favorite_language = {
    'tony': 'C',
    'tom': 'python',
    'peter': 'java',
}
for name,language in favorite_language.items():
    print(name.title()+"'s favourite language is "+language.upper())
friends = ['peter', 'tom']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("hi,"+name.title()+",i see your favourite language is "+favorite_language[name].title())

#偏历字典
user_0 = {
    'username': 'peter',
    'first': 'lily',
    'last': 'fermi',
}
for key,value in user_0.items(): #声明俩个变量，item()方法返回一个键值队列表
    print("keys: "+key)
    print("value: "+value)

for key in user_0.keys(): #遍历所以key
    print(key)
for name in user_0:
    print(name)
    print(user_0[name].upper()) #输出对应key的值使用字典



