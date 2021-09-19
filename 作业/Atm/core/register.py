# Auth: ShiHang
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def register_page():
    print("注册".center(30,"-"))
    while True:
        name = input("输入您的账号名称：")
        if len(name) <= 6:
            print("账号长度不能低于6位，请重新输入！")
            continue
        else:
            break
    while True:
        passwd = input("输入您的密码：")
        if len(passwd) < 6:
            print("账号密码长度不得低于6位，请重新输入！")
            continue
        else:
            break
    while True:
        tel = input("输入您的手机号码：")
        if len(tel) != 11 :
            print("手机号码输入错误，请重新输入！")
            continue
        else:
            break
    while True:
        emailnum = input("输入您的邮箱：")
        if "@" in emailnum:
            break
        else:
            print("邮箱输入错误，请重新输入！")
            continue
    data = (name,passwd,tel,emailnum)
    return data
# code = register_page()
# print(code)

def register_user(user,passwd,telphone,email):
    f = open("%s/db/account/%s.json" %(BASE_DIR,user),"w")
    data = {
        "username":user,
        "password":passwd,
        "tel":telphone,
        "emailaddr":email,
    }
    f.write(str(data))
    f.close()
    print("账号%s注册成功！" %user)
# register_user("shihang","123456","18910338786","530496304@qq.com")
# f = open("%s/db/account/count.json" %BASE_DIR,"r")
# data = eval(f.read())
# print(type(data))
# print(data["username"])