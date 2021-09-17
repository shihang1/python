# Author: ShiHang
# 装饰器：本质是函数（装饰其它函数）
# 就是为其他函数添加附加功能
# 原则：
# 1、不能修改被装饰的函数的源代码
# 2、不能修改被装饰的函数的调用方式

# 实现装饰器知识储备：
# 1、函数即变量
# 2、高阶函数
# 3、嵌套函数
# 高阶函数+嵌套函数 =》 装饰器

import time
def timeer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return  warpper


@timeer
def test1():
    time.sleep(3)
    print("in the test1")
test1()