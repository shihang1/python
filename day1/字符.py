# Author: ShiHang
#-*- coding:utf-8 -*-
#python3.0默认unioncode

a = '我是中国人'
print("a",a)
b = a.encode("utf-8")
print("b",b)
c = a.encode("gbk")
print(("c",c))
d = c.decode("gbk")
print("d",d)
e = c.decode("gbk").encode("utf-8").decode("utf-8").encode("gb2312")
print("e",e)