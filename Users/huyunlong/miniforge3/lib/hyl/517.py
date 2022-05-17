alien = {'x_position' :2,'y_position' :25,'speed': 'medium'}
print("original x_position: "+str(alien['x_position']))
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'fast':
    x_increment = 3
else:
    x_increment = 2
alien['x_position'] = alien['x_position'] + x_increment
print("new x_position: "+str(alien['x_position']))