# Author: ShiHang
name = "this is a test,please check it!"
name2 = "this is a test,\tplease check it!"
name3 = "this is a {i},please check {y}!"
name1 = "-"

print(name.count('a'))   #统计字符数量
print(name.capitalize())   #首字母大写
print(name.center(50,'-'))
print(name1.center(50,'-'))   #打印50个字符
print(name.endswith("it!"))   #以什么结尾
print(name2.expandtabs(tabsize=20))   #转换成多少个空格
print(name[name.find("test"):])   #切片
print(name.format(i="test",y="it"))  #格式化
print(name.format_map({'i':'y','test':'it'}))   #字典
print('123'.isalnum())  #判断是否包含字母或数字
print('abs2'.isalpha())   #判断是否是纯英文字符
print('1384734A'.isdecimal())    #是否为10进制数
print('212'.isdigit())   #判断是够为整数
print('_a2121'.isidentifier())   #判断是不是一个合法的标志符
print('3412.213'.isnumeric())   #判断是否为一个数字,只能是数字
print(' '.isspace())  #判断是否是一个空格
print('Mhis Is'.istitle())   #每个字母大写
print('My name '.isprintable())  #tty file，drive file 无法打印的
print('MY I'.isupper())   #判断是否为大写
print('hehe'.join("++++++"))
print('|'.join(['1','2','3','4'])) #合成字符串
print(name.ljust(50,'-'))  #长度50.不够用-符号不上,左侧补
print(name.rjust(50,'-'))  #长度50.不够用-符号不上,右侧补
print("alEs".lower())  #转换成小写
print('ALse'.upper())  #转换成大写
print('shsAHSi\n'.lstrip())  #从左边去掉回车和空格
print(name1.center(50,'-'))
print('\nshsAHSi\n'.rstrip())  #从右边去掉回车和空格
print(name1.center(50,'-'))
print('\ns    hsAHSi\n'.strip())  #从两侧去掉回车和空格
print(name1.center(50,'-'))
p = str.maketrans('abdsdfwew','123456789')    #字符替换，可以用于密码替换
print('sdsgabfds'.translate(p))
print('232sds'.replace('s','F',1))  #只替换一个
print('dascsd2'.rfind('d'))   #最右边的下标
print('ds ads ad'.split('a'))   #分割成列表
print('|'.join(['1','2','3','4']))
print((('|'.join(['1','2','3','4']))).split('|'))
print('1+2\n+3+4'.splitlines()) #换行符分割
print('shaisaSDSD'.swapcase())  #大小写互相转换
print('sdsSSD'.zfill(22))   #不够前补0