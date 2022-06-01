###文件和异常
##从文件中读取数据
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

##文件路径

