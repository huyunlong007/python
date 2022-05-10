#title()以首字母大写显示每个单词
name="my love, dragon"
print(name.title())
print(name.upper())
print(name.lower())

#字符串拼接
first_name=" "
last_name="my love"
full_name=first_name+","+last_name
print(full_name.title()+"!")

print("\thello world")

#去除空白
language='  python  '
print(language.rstrip())
print(language.lstrip())
print(language.strip())

#练习
human_name='eric'
print("hello "+human_name.title()+", would u like to learn some python today!")

#整数、浮点数
def sum():
    print(sum(range(1,101)))

