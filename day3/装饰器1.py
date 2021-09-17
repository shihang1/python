# Author: ShiHang
import time
def Tet(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func running time:%s" %(stop_time-start_time))
    return deco
@Tet
def test1():
    time.sleep(2)
    print("in the test1")
test1()
@Tet   #相当于test2=Tet（test2） 即test2（）=deco（），没有参数
def test2(name,haha):
    time.sleep(2)
    print("in the test2",name,haha)
test2("hehe","enene")
# test1=Tet(test1)
# print(test1)
# test1()
# test2()
# test1=deco(test1)
# test1()
# print(test1)
# deco(test2)





