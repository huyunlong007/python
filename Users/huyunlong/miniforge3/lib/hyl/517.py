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

##按照顺序遍历字典sorted()方法
favorite_language = {
    'jay': 'python',
    'kris': 'C#',
    'jeray': 'java',
}
for name in sorted(favorite_language.keys()):  #sorted()函数按
    print(name.title()+", thank you for taking the poll")

favorite_language['tony'] = 'python' #字典添加键值
print(favorite_language)
#使用value()方法
for language in favorite_language.values():
    print(language.upper())
for language in set(favorite_language.values()):  #使用set()方法去重复值
    print(language.upper())

####嵌套
aliens = []
for new_alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'fast'}
    aliens.append(new_alien)
    print(aliens)
for alien in aliens[:-1]:
    print(alien)
print("totol number of aliens: "+str(len(aliens)))
##
aliens = []
for new_alien in range(0,30):
    new_alien = {'color': 'green', 'points': 7, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 27
    elif alien['color'] == 'yellow':
        alien['speed'] = 'fast'
        alien['points'] = 28
for alien in aliens[0:5]:
    print(alien)

###在字典中存储列表




