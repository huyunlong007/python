###文件和异常
##从文件中读取数据
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

##文件路径
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
##
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()  #readline()方法读取文件中每一行
for line in lines:
    print(line.rstrip())

##
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()
pi_string = ''
for line in lines:
    pi_string += line.strip() #使用循环将各行加入pi_string
birthday = input("enter your birthday, in the form mmddyy")
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print(" ")
#print(pi_string[:8]+"...")
#print(len(pi_string))




