# Author: ShiHang
list = set([1,3,4,5,1,2,5,343,])

# print(set(list),type(set(list)))

list_1 = set([2,3,4,7,3,223,12])

list_2 = set([1,6,5])
print(list_1,list)

a = list_1.intersection(list)  #交集
print(a)
print(list_1 & list)

b = list_1.union(list)  #并集
print(b)
print(list_1 | list)

c = list_1.difference(list)  #差集，1跟2不同的
print(c)
print(list_1 - list)
print(list - list_1)

d = list.difference(list_1)  #差集，1跟2不同的
print(d)

e = list.issubset(list_2)
print(e)
e = list_2.issubset(list) #前者是后者的子集
print(e)
e = list.issuperset(list_2)
print(e)
e = list_2.issuperset(list) #前者是后者的父集
print(e)

f = list.symmetric_difference(list_1)  #对称差集
print(f)
print( list ^ list_1)

print("--------------------")
f = list_2.isdisjoint(list_1)  #如果没有交集，则返回true，有交集返回false
print(f)

# list.add(999)   #添加一项
# print(list)
# list.update([223,23,232,399])   #添加多项
# print(list)

# list.remove(23)  #指定删除
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
print(list)
list.discard(22)  #删除，没有也不报错，remove没有会报错
print(list)
#
# print(len(list))  #列表长度
#
# print(2 in list)   #在列表中
# print(2 not in list)    #不在列表中
