# Author: ShiHang
# 函数内部可以调用其它函数，也可以调用自己，这个函数就叫做递归函数
# 递归的特性：
# 1、必须有明确的结束条件
# 2、最大递归999层
# 3、每次进入更深一层递归时，问题规模相比上次递归都应有所减少
# 4、递归效率不高，递归层次过多会导致溢出（在计算机中，函数调用是通过stack栈这种数据结构实现的，每当进入一个函数调用，栈数就会增加一层栈帧，每当函数返回，栈就会减一层栈帧，由于栈的大小不是无限的
# 所有递归的调用次数过多，会导致栈溢出
#
#
# def dac(n):
#     print(n)
#     if int(n) > 2:
#         dac(int(n/2))
#     else:
#         return n
# x=dac(10)
# # print(x)
#
# a=int(5/2)
# print(a,"a")

sum = 0
def dec(n):
    global sum
    if n <= 100:
        sum += n
        dec(n+1)
    return sum
a=dec(99)
print(a)


def exe(a,b,f):
    y=f(a)+f(b)
    print(y)
exe(1,-22,abs)