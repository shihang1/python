# Auth: ShiHang
# 生成器，只有在调用时才会生成对应的数据,只能一个一个往后生成数据，
#只记录当前的位置
#只有一个__next__()方法
item = []
a = (10*x for x in range(1000))  #生成方法一
# for x in a:
#     item.append(x)
# print(item[2])
# print(a)
# print(a.__next__())
# 0 1 1 2
def fib(max):
    a,b,c=0,0,1
    while a < max:
        # print(c)
        yield c   #函数生成器的关键，函数中断，保存了函数终端状态
        b,c=c,b+c
        a +=1
    return "ok"
# num = 10
# i=1
a=fib(10)
#
# # while i <= num:
# # print(a.__next__())
i=1
# print("-----")
# for i in a:
#     print(i)

while i < 100:
    try:
        print(a.__next__())
    except StopIteration as e:
        print("haha:",e.value)
        break





