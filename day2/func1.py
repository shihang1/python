# Author: ShiHang

def funct1():
    a=1
    sum=0
    while a <= 100:
        sum = sum + a
        a = a + 1
    print(sum)
    return sum,'hello',['haha','hehe'],{'haah':'heeh'}
# funct1()
# x=funct1()
# print(x)

#返回值数量=0，返回NULL
#返回值数量=1，返回object（对象）
#返回值数量>1，返回元组

def funct2(x,y):
    sum = 0
    while x <= y:
        sum = sum + x
        x += 1
    print(sum)
# funct2(1,10)   #与形参一一对应
funct2(y=100,x=1)   #与形参顺序无关
# funct2(1,y=10)   #可以执行
# funct2(x=1,10)  #不可以执行，10会赋值给x
# funct2(1,x=10)   #不可以执行


def funct3(x,y=2):
    print(x)
    print(y)
funct3(1,3)  #y按照实际入参显示
funct3(1)  #y是默认参数
# a=1
# b=30
# funct1(x=a,y=b)

#默认参数特点：调用函数的时候，默认参数非必须传递
#用途：1、默认安装值






