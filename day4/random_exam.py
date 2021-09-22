# Author: ShiHang
import random
print(random.random())  #0到1的随机数，浮点数
# print(help(random))
print(random.randint(1,100))  #1到100的随机数
print(random.randrange(1,100,2))
print(random.choice('helloworld'))
print(random.choice([1,2,3,4,5,6]))  #可以元组、字符串、列表等
print(random.sample('hello',3))  #随机取几位
print(random.uniform(1,10))   #选择范围的取浮点数

#洗牌
items=[1,2,3,4,5,6,7,8]
print(items)
random.shuffle(items)
print(items)

#验证码
print('分隔符'.center(50,'-'))
final_current=''

for i in range(0,4):
    current = random.randint(0,4)
    if current == i:
        current = chr(random.randint(65,90))
    else:
        current = random.randint(0,9)
    final_current += str(current)
print(final_current)
