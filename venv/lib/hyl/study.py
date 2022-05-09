
message="hello,world!"
print(message)

simple_message="i believe i can fly!"
print(simple_message)

for i in range(1,10):
    for j in range(1,i+1):
       print('%s*%s=%s'%(i,j,i*j),end='')
    print()
