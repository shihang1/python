# Author: ShiHang
#匿名函数，没有引用，内存立马回收

cal = lambda x,y:x+y

result = cal(3,4)
print(result)