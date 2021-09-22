# Author: ShiHang
import sys_exam

1、定义：
模块：本质就是.py结尾的python文件，用来从逻辑行组织python代码（变量，函数，类，逻辑，实现一个功能）文件名test.py,模块名为test
包：本质就是一个目录（必须带有一个__init__.py文件，用来从逻辑上组织模块

2、使用方法
import test
import test,test1
from test import *    #(导入所有的)
from test import test1,test2,test3
from test import logger as module

3、import本质（路径搜索和搜索路径）
导入模块的本质就是把python文件解释一遍
import module_name -----> module_name.py  ------> module_name.py的路径---->sys_exam.path

导入包的本质就是执行该目录下的__init__.py文件

4、导入优化
from module_test import test

5、模块分类
a.标准库
b.开源模块
c.自定义模块