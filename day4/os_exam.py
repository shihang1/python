# Auth: ShiHang
#-*- coding:utf-8 -*-

import os
print('分隔符'.center(50,'-'))

print(os.getcwd()) #获取当前工作目录，即当前python脚本工作的目录路径
print('分隔符'.center(50,'-'))

os.chdir("C:\\Users\\小球\\PycharmProjects\\test\\day3")  #改变当前目录方法一
print(os.getcwd())
os.chdir(r"C:\Users\小球\PycharmProjects\test\day2")  #改变当前目录方法二
print(os.getcwd())
print('分隔符'.center(50,'-'))

os.curdir
print(os.getcwd())   #获取当前目录的父目录
print('分隔符'.center(50,'-'))

print(os.pardir)
print('分隔符'.center(50,'-'))

# os.makedirs(r'C:\a\b')   #创建目录
# os.chdir(r'C:\a\b')
# print(os.getcwd())
# os.chdir(r"C:\Users\A\PycharmProjects\python\day2")
print('分隔符'.center(50,'-'))

# os.removedirs(r'C:\a\b')  #删除目录
print('分隔符'.center(50,'-'))

# os.mkdir(r'E:\a')
# os.mkdir(r'E:\a\b') #逐层创建目录
# os.chdir(r'E:\a\b')
# os.rmdir(r'E:\a\b')
# os.rmdir(r'E:\a')
print(os.getcwd())
print('分隔符'.center(50,'-'))

print(os.listdir())  #显示当前目录所有文件
print('分隔符'.center(50,'-'))

# os.remove()  #删除一个文件
print('分隔符'.center(50,'-'))

# os.rename("oldname"."newname") #文件重命名
print('分隔符'.center(50,'-'))

print(os.stat(r'func1.py'))   #获取文件属性
print(os.stat(os.getcwd()))   #获取目录属性
print('分隔符'.center(50,'-'))

print(os.sep)  #获取操作系统的特定路径分隔符,windows为\  linux为/
print(os.linesep)  #获取当前平台使用的终止符，windows为\t\n linux为\n
print(os.pathsep)  #获取用于分割文件路径的字符串，win为； linux为：
print('分隔符'.center(50,'-'))

print(os.name)   #win下为nt  linux为posix
print('分隔符'.center(50,'-'))

print(os.environ)   #获取系统环境变量
print('分隔符'.center(50,'-'))

# os.system('dir')
# os.system('ipconfig')  #执行系统命令
print('分隔符'.center(50,'-'))

print(os.path.abspath(__file__))  #获取当前文件的路径，返回path规范化的绝对路径
print('分隔符'.center(50,'-'))

print(os.path.split(os.path.abspath(__file__)))  #将文件名与路径分割
print('分隔符'.center(50,'-'))

print(os.path.dirname(__file__))  #返回path的目录，其实就是os.path.split的第一个元素
print('分隔符'.center(50,'-'))

print(os.path.basename(__file__))  #返回path的目录，其实就是os.path.split的第二个元素,如果以\或者/结尾，则返回控制
print('分隔符'.center(50,'-'))

print(os.path.exists(os.path.dirname(__file__)))  #目录存在则返回true，不存在则返回false
print(os.path.exists(r'D:\a'))
print('分隔符'.center(50,'-'))

print(os.path.isabs(os.path.dirname(__file__)))  #绝对路径则true 不是则false
print(os.path.isabs('..'))
print('分隔符'.center(50,'-'))

print(os.path.isfile('作业-修改配置文件.py'))  #文件存在则true 不存在则false
print(os.path.isfile('test'))
print('分隔符'.center(50,'-'))

print(os.path.isdir(os.path.dirname(__file__)))  #是目录则true 不是目录则false
print(os.path.isdir(os.path.abspath(__file__)))
print('分隔符'.center(50,'-'))

print(os.path.join(r'E:',r'\a',r'\c',r'text.txt'))  #将多个目录组合返回，第一个绝对路径之前的参数将被忽略
# 1.如果各组件名首字母不包含’/’，则函数会自动加上
# 2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
# 3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾
print('分隔符'.center(50,'-'))

print(os.path.getatime(os.path.abspath(__file__))) #获取path所指文件或目录的最后存取时间
print(os.path.getmtime(os.path.abspath(__file__)))  #获取path所指向的文件或者目录最后修改时间
import time,datetime
item1=os.path.getatime(os.path.abspath(__file__))
item2=os.path.getmtime(os.path.abspath(__file__))
print(time.ctime(item2))
print(datetime.date.fromtimestamp(item1))
print('分隔符'.center(50,'-'))