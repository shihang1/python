# Auth: ShiHang
import json   #系统自带模块名和文件名一定不能一样
def func(name):
    print("ahah",name)

info={"name":"shiahng","age":23,"test":func}  #这不是一个可序列化的json格式，只能处理简单的数据格式，很多语言通用的，不同语言的类不一样
# print(func("test"))
# print(info)
f = open("test.txt",'w')
# # f.write(str(info))
# # f.close()
#
f.write(json.dumps(info))
f.close()


