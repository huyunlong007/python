##写入文件
filename = 'programing.txt'
with open(filename, 'a') as file_object:  #第一个实参为'w'写入模式打开文件
    file_object.write("i love you.\n")
    file_object.write("i will be work out.\n")

##小练习
name = 'guest_book.txt'
reason = "please tell me why you like to process:"
with open(name, 'w') as file_object:
    while True:
        message = input(reason)
        #print("hello, " + message)
        if message != 'quit':
            file_object.write("your reason is "+message+"\n")
        elif message == 'quit':
            break
        False
