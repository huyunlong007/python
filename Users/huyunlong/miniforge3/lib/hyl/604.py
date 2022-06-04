##写入文件
filename = 'programing.txt'
with open(filename, 'a') as file_object:  #第一个实参为'w'写入模式打开文件
    file_object.write("i love you.\n")
    file_object.write("i will be work out.\n")

##小练习
name = 'guest.txt'
with open(name, 'w') as file_name:
    file_name.write("what's your name")