# Author: ShiHang
import sys,os
print(sys.path)   #返回模块的搜索路径，初始化使用pythonpath环境变量的值
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_os=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path_os)
sys.path.append(path_os)
print(sys.path)
print("分隔符".center(50,'-'))
print(sys.argv[0])   #命令行参数，第一个元素是程序本身路径

print("分隔符".center(50,'-'))
print(sys.version)  #获取python解释程序的版本信息

print(len(str(sys.maxsize)))   #最大长度

print(sys.platform)  #返回系统平台名称

print(sys.getdefaultencoding())  #获取系统当前编码

print(sys.modules.keys())  #已经加载的模块的字典

s='abc'
try:
    int(s)
except ValueError:
    e = sys.exc_info()

print(type(e))