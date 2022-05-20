#whlie循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#1到100相加
sum = 0
i = 0
while i <= 100:
    sum = sum + i
    i += 1
print(sum)

#
'''
prompt = "tell me something,and i will repeat it back to you: "
prompt += "\nenter the 'quit' to end the program " #+=是上面输入下面提示
message = ''   #创建变量，定义一个初始值
while message != 'quit':   #判断变量并循环
    message = input(prompt)
    if message != 'quit':
        print(message)
'''
#使用标志用于判断整个程序是否处于活动状态
'''
prompt = "tell me something,and i will repeat it back to you: "
prompt += "\nenter the 'quit' to end the program " #+=是上面输入下面提示
active = True  #使用True标志最为变量
while active:
    message = input(prompt)
    if message == 'quit':  #若输入为'quit'则将变量置为false
        active = False
    else:
        print(message)
'''
#break中断while循环
'''
prompt = "tell me something,and i will repeat it back to you: "
prompt += "\nenter the 'quit' to end the program " #+=是上面输入下面提示
while True:
    message = input(prompt)
    if message == 'quit':  #若输入为'quit'则将变量置为false
        break
    else:
        print(message)
'''
#在while循环中使用continue
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 3 != 0: #不能被3整除
        continue  #
    print(current_number)

#小练习
'''
message = "please tell us your age: "
while True:
    age = input(message)
    age = int(age)
    if 0 < age < 3:
        ticket_prace = 0
    elif age >12:
        ticket_prace = 15
    elif 3 <= age <= 12:
        ticket_prace = 10
    elif age < 0:
        break
    print("your age is "+str(age)+",ticket_price is "+str(ticket_prace)+" dollows!")
'''
#active
''''
message = "please tell us your age: "
active = True
while active:
    age = input(message)
    age = int(age)
    if 0 < age < 3:
        ticket_prace = 0
    elif age >12:
        ticket_prace = 15
    elif 3 <= age <= 12:
        ticket_prace = 10
    elif age < 0:
        active = False
    print("your age is "+str(age)+",ticket_price is "+str(ticket_prace)+" dollows!")
'''
#使用while循环处理字典和列表







