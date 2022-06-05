##异常try-except代码块处理异常
try:
    print(7/0)
except ZeroDivisionError:
    print("you can't divide by zero")

##使用异常避免崩溃
print("please give me two numbers,and i'll divide them")
print("enter 'q' to end.")
while True:
    first_number = input("\nfirst number:")
    if first_number == 'q':
        break
    second_number = input("\nsecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:  #处理不能除以0的问题
        print("you can't divide by zero")
    else:
        print(answer)

##处理filenotfounderror
filename = 'hyl.txt'
try:
    with open(filename) as f_object:
        contents = f_object.read()
except FileNotFoundError:  #文件不存在
    msg = "sorry,the file "+filename+"doesn't exist."
    print(msg)

##使用多个文件count_words()函数
def count_words(filename): #计算文件大致包含多少个单词
    try:
        with open(filename) as f_ojt:
            contents = f_ojt.read()
    except FileNotFoundError:
        msg = "sorry,the file " + filename + "doesn't exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("the file "+filename+"has about"+str(num_words)+"words.")
filename = 'alice.txt'
count_words(filename)












