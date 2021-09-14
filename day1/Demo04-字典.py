# Author: ShiHang
info = {
    'std1001':"shihang",
    'std1002':"fangming",
    'std1003':"fanghang",
}

info1 = {
    'std1001':"hehe",
    3:5,
    4:4,
}

info.update(info1)  #有则更改，无则添加
print(info)
a = dict.fromkeys([3,2,3],[4,5,6]) #初始化一个新的字典，
print(a)
a[2][0] = "test"  #将所有修改，3个key共享一个内存地址，修改完之后将全部修改
print(a)
# print(info["std1001"])
# info["std1001"]="shiming"  #存在即修改，不存在则新建
# print(info["std1001"])
# # del info["std1001"]   #删除
# # print(info["std1001"])
# # info.pop("std1001")   #删除
# # print(info["std1001"])
# # info.popitem()   #随机删除
# # print(info)
#
# print(info.get('std004'))   #获取值，不存在则显示NONE
# print(info.get('std1001'))
#
# print('std10022' in info)  #判断是否存在

