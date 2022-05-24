##函数
def greet_user():  #def定义一个函数
    print("happy everyday!")
greet_user()
#
def greet_user(username):
    print("hello,"+username.title()+"!")
greet_user("HYL") #调用函数并传递参数

#实参和形参
def display_message():
    print("this part is hanhu")
display_message()
#
def favorite_book(title):
    print("One of my favorite books is "+title.title()+" in the wonderland")
favorite_book("alice")

###传递实参
#位置实参
def describe_pet(animal_type,pet_name='snake'): #形参
    print("\ni have a "+animal_type)
    print("my "+animal_type+"'s name is "+pet_name)
describe_pet("dog","senba") #对应位置实参
describe_pet("cat","jerry")

#关键字实参
describe_pet(animal_type='pig',pet_name='peiqi')

#默认值 #使用默认值形参时，先列出没有默认值的形参，再列有默认值的形参
describe_pet(animal_type='snake')

#小练习
def make_shirt(size,typle='love python'):
    print("\nthis shirt's size is "+size)
    print("its typle is "+typle)
make_shirt("M","iron-man")
make_shirt(size='XS',typle='captaial-cn')
make_shirt("大号") #默认字样的大号衬衫
make_shirt("XXL", "iron-man")


##返回值
def get_formatted_name(first_name, last_name, middle_name = ''): #
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()  #将结果返回到函数调用行
musician = get_formatted_name('joln', 'lee', 'stark')  #调用返回值的函数时，需要提供一个变量，用于存储返回的值
print(musician)
musician = get_formatted_name('H', 'Dragon')
print(musician)














