###存储数据
import json
numbers = [2, 3, 5, 7, 11, 13, 19]
filename = 'number.json'
with open(filename, 'w') as f_obt:
    json.dump(numbers, f_obt)  #json.dump()来存储这组数据

##
import json
filename = 'number.json'  #确保读取的是写入的文件
with open(filename) as f_obj:  #打开这个文件
    numbers = json.load(f_obj)  #json.load()函数来加载存储在numbers的数据
print(numbers)


##保存和读取用户生成的数据
import json
username = input("what's your name?")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(filename, f_obj)
    print("we'll remember you when you come back, "+username+"!")

#
import json
filename = 'username.json'
with open(filename) as f_obj:
    json.load(f_obj)
    print("welcome back,"+username+"!")



























