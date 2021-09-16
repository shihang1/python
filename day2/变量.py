# Author: ShiHang
# 局部变量,函数中，函数一般改不了全局变量，必须global
# 全局变量，一级目录中

#在子程序中定义的就是局部变量
#在程序一开始定义的变量是全局变量
#全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序
#当全局变量和局部变量同名时
#在定义局部变量的子程序内，局部变量起作用，在其它地方全局变量起作用



test = [1,2,3,4]
def change_name(hah):
    # global name
    # #修改全局变量，也可以定义全局变量，不建议在函数在定义全局变量
    test[2]=888
    print("before name :",name)
    print(test[2])
    print("after name :",name)
#列表、字典、集合、元组等复杂的都是可以在函数内更改全局变量的
#只有字符串、整数不能修改
name = 'fangming'
change_name(name)
print(name)
print(test[2])
