#传递列表
def greet_users(names):
    for name in names:
        msg = "hello, "+name.title()+"!"
        print(msg)
usernames = ['tony', 'jerry']
greet_users(usernames)

#在函数中修改列表
def print_models(unprinted_designs, completed_designs):  #定义一个print_model函数
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model:"+current_design)
        completed_designs.append(current_design)
def show_completed_models(completed_models):
    print("\nthe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot']
completed_models = []
print(unprinted_designs,completed_models)
show_completed_models(completed_models)

#禁止修改函数列表
















