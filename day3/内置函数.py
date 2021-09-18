# Author: ShiHang
# abs	求绝对值 1、参数可以是整型，也可以是复数 2、若参数是负数，则返回负数的模
import functools

print(abs(-220))
print(abs(20))
print('分隔符'.center(50,'-'))

# all  	1、集合中的元素都为真的时候为真  2、特别的，若为空串返回为True
print(all([1,2,3]))
print(all([0,2,2]))
print('分隔符'.center(50,'-'))

# any 1、集合中的元素有一个为真的时候为真 2、特别的，若为空串返回为False
print(any([0]))
print(any([0,2,2]))
print('分隔符'.center(50,'-'))

#assii  转换成字符串
a=ascii([1,2,"这是一个测试！"])
print(a)
print(type(a))
print('分隔符'.center(50,'-'))

#bin  10进制转换2进制
print(bin(255))
print(bin(1))
print(bin(2))
print(bin(4))
print(bin(8))
print('分隔符'.center(50,'-'))

#boo 0为假，1为真
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([1]))
print('分隔符'.center(50,'-'))

# bytearray 字节数组   bytes 把字符串转成字节
item = bytes("absnds",encoding='utf-8')
item1 = bytearray("absnds",encoding='utf-8')
print(item.capitalize(),item)
print(item1[0])  #assii码值
print(item1[1])
item1[0]=56
print(item1)
print('分隔符'.center(50,'-'))

# callable	检查对象object是否可调用
# 1、类是可以被调用的
# 2、实例是不可以被调用的，除非类中声明了__call__方法
def func():pass
print(callable(func))
print(callable([]))
print('分隔符'.center(50,'-'))

# chr 打印出数字对应的assii码   ord  打印出对应的assii数字
print(chr(92))
print(chr(97))
print(chr(122))
print(ord('a'))
print(ord('z'))
print('分隔符'.center(50,'-'))

# classmethod 类方法

# compile(source, filename, mode[, flags[, dont_inherit]])
# 将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
# 1、参数source：字符串或者AST（Abstract Syntax Trees）对象。
# 2、参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# 3、参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
# 4、参数flag和dont_inherit：这两个参数暂不介绍

# complex 复数

# dir 字典,查出有什么方法可以使用
# 1、不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 2、带参数时，返回参数的属性、方法列表。
# 3、如果参数包含方法__dir__()，该方法将被调用。当参数为实例时。
# 4、如果参数不包含__dir__()，该方法将最大限度地收集参数信息
item1=()
print(dir(item))
print(dir())
print('分隔符'.center(50,'-'))

# divmod()  取余数
print(divmod(5,3))
print(divmod(5,5))
print('分隔符'.center(50,'-'))

# enumerate 返回一个可枚举的对象,该对象的next()方法将返回一个tuple
i = [1,2,3,4,5]
for index,line in enumerate(i):
    print(index,line)
print('分隔符'.center(50,'-'))

# eval 计算表达式expression的值  把字符串中的数据结构给提取出来
dirc=['haha','hehe']
sam=str(dirc)
print(type(sam))
print(type(dirc))
lin=eval(sam)
print(lin)
print(type(lin))
print('分隔符'.center(50,'-'))

# exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
code='for i in range(5):print("iter time: %d" % i)'
exec (code)
print('分隔符'.center(50,'-'))

# filter 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# map 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
def jisuan(x):
    print(x)
jisuan(5)
calc=lambda n:print(n**n)
calc(4)
a=filter(lambda n:n>5,range(10))
print(a)
for i in a:
    print(i)
b=map(lambda n:n**n,range(6))
print(b)
for i in b:
    print(i)
i=1
while i < 6:
    c=functools.reduce(lambda x,y:x+y,range(i))  #追加1+2+3+4+5
    print(c)
    i+=1
print('分隔符'.center(50,'-'))

# float 函数用于将整数和字符串转换成浮点数
a = 1
print(a)
print(float(a))
print('****'.center(50,'-'))

# format() python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。
print("{0} {1} {0}".format("hello","world"))
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
print("{:.2f}".format(3.1415926))
# 数字	格式	输出	描述
# 3.1415926	{:.2f}	3.14	保留小数点后两位
# 3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
# -1	{:+.2f}	-1.00	带符号保留小数点后两位
# 2.71828	{:.0f}	3	不带小数
# 5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)
# 5	{:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
# 10	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
# 1000000	{:,}	1,000,000	以逗号分隔的数字格式
# 0.25	{:.2%}	25.00%	百分比格式
# 1000000000	{:.2e}	1.00e+09	指数记法
# 13	{:>10d}	        13	右对齐 (默认, 宽度为10)
# 13	{:<10d}	13	左对齐 (宽度为10)
# 13	{:^10d}	    13	中间对齐 (宽度为10)
# 11
# '{:b}'.format(11) 1011
# '{:d}'.format(11) 11
# '{:o}'.format(11) 13
# '{:x}'.format(11) b
# '{:#x}'.format(11) 0xb
# '{:#X}'.format(11)	 0XB	进制
print('****'.center(50,'-'))

# frozenset 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
a = frozenset([1,4,4,53,32])
b = set([1,4,4,53,32])
# a[1]=2
# a.add(22)  AttributeError: 'frozenset' object has no attribute 'add'
print(a)
# print(a[1])
b.add(222)
print(b)
print('****'.center(50,'-'))

# getattr() 函数用于返回一个对象属性值



# globals() 函数会以字典类型返回当前位置的全部全局变量。
a=2
b=3
print(globals().get("__name__"))
aggr=globals()
print(aggr["a"])
# for i in aggr:
#     print(i)
print('globals'.center(50,'-'))


# hasattr() 函数用于判断对象是否包含对应的属性。
# hash() 用于获取取一个对象（字符串或者数值等）的哈希值
print(hash(12323))
sdshi=hash("aaaaaa")
print(sdshi)
print(hash(str([1,2,3])))
print(hash(str(sorted({1:2}))))
print("分隔符".center(50,'*'))


# help() 函数用于查看函数或模块用途的详细说明
# print(help(open))
print("分隔符".center(50,'*'))

# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
print(hex(31))
print("分隔符".center(50,'*'))

# id() 函数返回对象的唯一标识符，标识符是一个整数。
# CPython 中 id() 函数用于获取对象的内存地址
print(id(a))    #返回内存地址
print(id(1))
print(id(2))
print("分隔符".center(50,'*'))

# Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
# Python2.x 中 input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。
# raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。
# name =input("请输入：")
# 注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
# 而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
# 除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
# 注意：python3 里 input() 默认接收到的是 str 类型。
# print(type(name))
print("分隔符".center(50,'*'))
# 注意：在 Python3.x 中 raw_input() 和 input() 进行了整合，去除了 raw_input( )，仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。


# int() 函数用于将一个字符串或数字转换为整型。
# 以下是 int() 方法的语法:
# class int(x, base=10)
# x -- 字符串或数字。
# base -- 进制数，默认十进制。

a=int("abcd",16)  # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
print(a)
print("分隔符".center(50,'*'))



