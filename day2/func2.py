# Author: ShiHang
def test(*args):
    print(args)
test(1,2,3,4,3)
test(*[1,2,3,4,3])   #变成元组模式

def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,3,4)