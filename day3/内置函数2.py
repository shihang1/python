# Author: ShiHang

# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()
str1=1
print(isinstance(str1,int))
print(isinstance(str1,str))
str2="haha"
print(isinstance(str2,int))
print(isinstance(str2,str))
print(isinstance (str2,(str,int,list)))
print("isinstance".center(50,"-"))

# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。


# iter() 函数用来生成迭代器
# 以下是 iter() 方法的语法:
# iter(object,[sentinel])
# object -- 支持迭代的集合对象。
# sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
a={i for i in range(10)}
b=iter(a)
print(b.__next__())
print(b.__next__())
print("iter".center(50,"-"))

# len()方法返回对象（字符、列表、元组等）长度或项目个数
print(len("hdisfiffsd"))
print("len".center(50,"-"))

# list() 方法用于将元组转换为列表。
# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中
a=(1,2,3,4)
b=a
print(b)
c=list(a)
print(c)
print("list".center(50,"-"))

# locals() 函数会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
def func():
    sss=333
    print(locals())
    print(globals().get("sss"))
func()
print(globals().get("sss"))
print("locals".center(50,"-"))

# long() 函数将数字或字符串转换为一个长整型。
# Python3.x 版本已删除 long() 函数。
print("long".center(50,"-"))

# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
def test(x):
    return  x**x
print(test(2))
x=map(test,[i for i in range(10)])
y=map(lambda x:(2*x),[x for x in range(5)])
print(list(x)) #使用 list() 转换为列表
print(list(y))
print("map".center(50,"-"))

# max() 方法返回给定参数的最大值，参数可以为序列
# min() 方法返回给定参数的最小值，参数可以为序列
a=[1,232,2.333,232,656,31214,432]
print(max(a))
print(min(a))
print("max and min".center(50,"-"))

# memoryview() 函数返回给定参数的内存查看对象(memory view)。
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。
v = memoryview(bytearray("abcefg", 'utf-8'))
print(v[1])
print("memoryview".center(50,"-"))

# next() 返回迭代器的下一个项目。
# next() 函数要和生成迭代器的 iter() 函数一起使用
item=iter([x for x in range(10)])
print(next(item))
print(next(item))
print("iter".center(50,"-"))

# oct() 函数将一个整数转换成 8 进制字符串。
# Python2.x 版本的 8 进制以 0 作为前缀表示。
# Python3.x 版本的 8 进制以 0o 作为前缀表示。
num=9
print(oct(num))
print("oct".center(50,"-"))

# python open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
print("open".center(50,"-"))

# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
print(ord("a"))
print("ord".center(50,"-"))

# pow() 方法返回 xy（x 的 y 次方） 的值
print(pow(10,10))
print("pow".center(50,"-"))

# print() 方法用于打印输出，最常见的一个函数。在 Python3.3 版增加了 flush 关键字参数。
# 以下是 print() 方法的语法:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
# sep -- 用来间隔多个对象，默认值是一个空格。
# end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
# file -- 要写入的文件对象。
# flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
a=(121,2321,3,4,5,[1,2,3,4])
print("aaa","bbbb",sep="*")
for i in a:
    print(i,sep="*",end=" ")
print("loading",end="")
import time
# for i in range(20):
#     print(".",end=' ')
#     time.sleep(0.5)
print("")
print("print".center(50,"-"))


# property() 函数的作用是在新式类中返回属性值


# Python3 range() 返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表，具体可查阅 Python3 range() 用法说明。
# 函数语法
# range(start, stop[, step])
# 参数说明：
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
a=[x for x  in range(1,10,2)]
print(a)
print("range".center(50,"-"))

# reduce() 函数会对参数序列中元素进行累积。
# Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：
from functools import reduce
# reduce() 函数语法：
# reduce(function, iterable[, initializer])
# 参数
# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数
def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)
print("reduce".center(50,"-"))

# reload() 用于重新载入之前载入的模块
import importlib,sys
importlib.reload(sys)
print(sys.getdefaultencoding())
print("reload".center(50,"-"))

# repr() 函数将对象转化为供解释器读取的形式
item="hehe"
print(repr(item))   #用字符串表示这个对象
for i in repr(item):
    print(i)
print("repr".center(50,"-"))

# reverse() 函数用于反向列表中元素
a= [1,2,3,4]
a.reverse()
print(a)
print("reverse".center(50,"-"))

# round() 方法返回浮点数x的四舍五入值
# 以下是 round() 方法的语法:
# round( x [, n]  )
# x -- 数值表达式。
# n -- 数值表达式，表示从小数点位数。
print(round(5.32))
print(int(round(23235.2323,-2)))
print("round".center(50,"-"))

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
a=[56,2,3,4,5,2,3,4]
print(set(a))  #数字有序
b="google"
print(set(b))  #字母无序
print("set".center(50,"-"))

# setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的
# setattr() 语法：
# setattr(object, name, value)
# object -- 对象。
# name -- 字符串，对象属性。
# value -- 属性值。
print("setattr".center(50,"-"))

# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递
d=range(10)
print(d)
d=d[slice(2,5)]
for a in d:
    print(a)
print("slice".center(50,"-"))

# sorted() 函数对所有可迭代的对象进行排序操作。
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
# sorted 语法：
# sorted(iterable, cmp=None, key=None, reverse=False)
# 参数说明：
# iterable -- 可迭代对象。
# cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
a={3:2,11:212,343:1,2342:22,-5:23}
print(sorted(a))   #只排序key
print(sorted(a.items()))
print(sorted(a.items(),key=lambda x:x[1]))
print("sorted".center(50,"-"))


# python staticmethod 返回函数的静态方法。
# 该方法不强制要求传递参数，如下声明一个静态方法：
# class C(object):
#     @staticmethod
#     def f(arg1, arg2, ...):
#         ...
# 以上实例声明了静态方法 f，从而可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。
print("staticmethod".center(50,"-"))

# str() 函数将对象转化为适于人阅读的形式
a={"shihang","fangming","haha"}
print(str(a))
print(a)
print(type(a))
print(type(str(a)))
print("str".center(50,"-"))

# sum() 方法对序列进行求和计算
a=[0,1,2,3,4]
b=3
print(sum(a,b))
print("sum".center(50,"-"))


# super() 函数是用于调用父类(超类)的一个方法。
# super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
print("super".center(50,"-"))

# Python 元组 tuple() 函数将列表转换为元组
a=[1,2,3,4]
print(tuple(a))
print(type(a))
print(type(tuple(a)))
print("tuple".center(50,"-"))

# type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
# sinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
# 语法
# 以下是 type() 方法的语法:
# type(object)
# type(name, bases, dict)
# name -- 类的名称。
# bases -- 基类的元组。
# dict -- 字典，类内定义的命名空间变量。
print("type".center(50,"-"))

# unichr() 函数 和 chr() 函数功能基本一样， 只不过是返回 unicode 的字符。
# 注意： Python3 不支持 unichr()，改用 chr() 函数。
print("unichr".center(50,"-"))

# vars() 函数返回对象object的属性和属性值的字典对象
# 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()
print(vars())
class A:
    print("haha")
print(vars(A))
print("vars".center(50,"-"))

# xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器
# 因为 python3 中取消了 range 函数，而把 xrange 函数重命名为 range，所以现在直接用 range 函数即可
print("xrange".center(50,"-"))

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
a=[1,2,3,4,5]
b=["a","b","c","d","e","f"]
c=zip(a,b)  #按照数量少的组合
for i in c:
    print(i,end= ' ')
print(" ")
print("zip".center(50,"-"))

# __import__() 函数用于动态加载类和函数 。
# 如果一个模块经常变化就可以使用 __import__() 来动态载入。
__import__('test')
print("__import__".center(50,"-"))