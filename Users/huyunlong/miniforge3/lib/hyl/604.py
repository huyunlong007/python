##写入文件
filename = 'programing.txt'
with open(filename, 'w') as file_object:  #第一个实参为'w'写入模式打开文件
    file_object.write("i love you")