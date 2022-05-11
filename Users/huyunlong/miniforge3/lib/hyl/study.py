
message="hello,world!"
print(message)

simple_message="i believe i can fly!"
print(simple_message)
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
       print('%s*%s=%s'%(i,j,i*j),end=' ')
    print()

#1到100相加for循环
def sum():
    sum=0
    for i in range(1,101):
       sum=sum+i
    return sum
print(sum())

#方法二 使用while循环
i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

#方法三 使用sum和range函数
def sum():
    print(sum(range(1,101)))