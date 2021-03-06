# Auth: ShiHang
# 可作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list，tuple，dict，set，str等
# 一类是generator，包括生成器和带yield的generate function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()判断一个对象是否是Iterable对象

from collections.abc import Iterable
from collections.abc import Iterator
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abcssdsds',Iterable))
print(isinstance((i for i in range(10)),Iterable))
print(isinstance(100,Iterable))
print("-------------")

# 生成器不但可以作用于for循环，还可以被next（）函数不断调用并换回下一个值
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# *可以被next（）函数调用并不断返回下一个值得对象称为迭代器：Iterator
# 可以使用isinstancer（）判断一个对象是否是Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abcssdsds',Iterator))
print(isinstance((i for i in range(10)),Iterator))
print("-------------")

# 生成器都是Iterator对象，但list,dict,str虽然是Iterable，缺不是Iterator
# 把list，dict，str等Iterable编程Iterator可以使用iter（）函数

print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abcssdsds'),Iterator))
a=[1,2,3]
b=iter(a)
print(b)
print(b.__next__())
print(b.__next__())
print(b.__next__())

# python的Iterator对象表示的是一个数据流，Iterator对象可以被next（）函数调用并不断返回下一个数据，知道没有数据是抛出StopIteration错误
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道这个序列的长度，只能不断通过next（）函数实现按需计算下一个数据
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而使用list是永远不可能存储全体自然数的。


# 小结：
# 凡是可以作用于for循环的对象都是Iterable类型
# 凡是可以作用于next（）函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list，dict，str等是Iterable但是不是Iterator，不过可以通过iter（）函数获得一个Iterator对象

print("**********")
for i in [1,2,3,4,5]:
    pass
#等价于
i = iter([1,2,3,4,5])

while True:
    try:
        print(i.__next__())
    except StopIteration as t:
        print(t.value)
        break




