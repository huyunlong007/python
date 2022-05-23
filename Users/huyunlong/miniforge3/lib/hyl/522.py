#用while循环处理列表和字典
unconfirmed_users = ['xiaoming', 'xiaoqiang', 'xiaozhang']
confirmed_users = []
while unconfirmed_users:  #循环验证未确认的用户
    current_user = unconfirmed_users.pop()  #pop()函数每次从后面删除一个未确认的用户
    print("verifying user: "+current_user.title())
    confirmed_users.append(current_user)  #
print("\nthe following users been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除包含特定值的所有列表元素
pets = ['cat', 'dog', 'goldfish', 'cat', 'dog']
print(pets)
while 'cat' in pets:
    pets.remove('cat') #remove()函数
print(pets)

#
'''
responses = {}
polling_active = True
while polling_active:
    name = input("\nwhat's your name?")
    response = input("which mountain would you like to climb somgday?")
    responses[name] = response  #把答卷键值存储到字典中
    repeat = input("would you like to want to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n ------poll result--------")
for name,response in responses.items():
    print(name+" would you like to climb "+response)
'''
#小练习
sandwich_orders = ['可爱多', '巧乐兹', '哈根达斯']
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("verifying order: "+current_order)
    finished_sandwiches.append(current_order)
print("\n the following orders been confirmed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


















