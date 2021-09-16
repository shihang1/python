# Author: ShiHang
# def test(*args):
#     print(args)
# test(1,2,3,4,3)
# test(*[1,2,3,4,3])   #变成元组模式
#
# def test1(x,*args):   #*args  接受的是位置参数，不能接收关键字参数
#     print(x)
#     print(args)
#
# test1(1,2,3,3,4)

def test3(name,**kwargs):
    print(name)
    print(kwargs)
    test2(name="shihang", age=22, sexy="man")
# test3("shihang",age=32)   #函数最好按顺序编写

def test2(**kwargs):    #**kwagrs  接收关键字参数
    print(kwargs)
    return kwargs
# x=test2(name="shihang",age=22,sexy="man") #转换成字典形式
# print(x["name"])

# def test3(name,**kwargs):
#     print(name)
#     print(kwargs)
#     test2(name="shihang", age=22, sexy="man")
# test3("shihang",age=32)

