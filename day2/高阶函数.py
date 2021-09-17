# Author: ShiHang
#函数传入参数
# def add(x,y,f):
#     return f(x) + f(y)
# ras = add(3,-25,abs)
# print(ras)
import time


# def func():
#     time.sleep(0.1)
#     print("this is a test!")
# # func()
# # print(func)   #内存地址
#
# def func1(item):
#     start_time=time.time()
#     func()
#     stop_time = time.time()
#     print("start_time:",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(start_time)))
#     print("stop_time:",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(stop_time)))
#     print("time is :%s" %(stop_time-start_time))
#
# func1(func)


def test1():
    print("haha!")
def test2(item):
    print(item)
    # test1()
    return item
print(test2(test1))
t=test2(test1)
t()
# print(t())

