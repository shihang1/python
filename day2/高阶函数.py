# Author: ShiHang
#函数传入参数
def add(x,y,f):
    return f(x) + f(y)
ras = add(3,-25,abs)
print(ras)