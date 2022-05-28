###将函数存储在模块中
##导入整个模块
import pizza
pizza.make_pizza(11, 'pepperoni') #module_name.function_name()
pizza.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

#导入特定的函数
from pizza import make_pizza
make_pizza(111, 'pepperoni') #直接使用函数不要加上脚本名称
make_pizza(152, 'mushrooms', 'green peppers', 'extra cheese')

#使用AS给函数指定别名
from pizza import make_pizza as mp  #as代替函数别名
mp(111, 'pepperoni')
mp(152, 'mushrooms', 'green peppers', 'extra cheese')
#使用AS给模块指定别名
import pizza as p
p.make_pizza(123, 'dragon')


#导入模块中所有函数
from pizza import *  #使用（*）运算符可导入模块中所有函数
make_pizza(1128, 'iPhone 13 Pro Max')

#小练习













