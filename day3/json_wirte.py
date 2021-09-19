# Auth: ShiHang
import json   #系统自带模块名和文件名一定不能一样
def func(name):
    print("ahah",name)
    # return name

# info={"name":"shiahng","age":23,"test":func("haha")}  #这不是一个可序列化的json格式，只能处理简单的数据格式，很多语言通用的，不同语言的类不一样
# # print(func("test"))
# # print(info)
# f = open("test.txt",'w')
# # # f.write(str(info))
# # # f.close()
# #
# f.write(json.dumps(info))
# f.close()


# 想处理复杂的使用pickle
import pickle   #只能在python在中使用，其它语言不识别
def func(name):
    print("ahah",name)
info1={"name":"shiahng","age":23,"test":func}
f = open("test1.txt",'wb')
pickle.dumps(info1,f)   #就相当于f.write(pickle.dumps(info1))


#只dumps一次，load一次
#要多次存，就写成多个文件