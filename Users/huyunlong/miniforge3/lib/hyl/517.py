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



