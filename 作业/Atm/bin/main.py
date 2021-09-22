# Auth: ShiHang
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import register
import loginpage,index

user_data = {
    "id":"none",
    "pawd":"none",
}

#账号信息，写入内存，防止用户绕过主页面登录
while True:
    loginpage.login_in()
    choice_num_login = int(input("输入您的选择："))
    # print(choice_num_login,type(choice_num_login))
    while True:
        if choice_num_login == 1:
            if user_data["id"] != "none" and user_data["pawd"] != "none":
                if auth_data == 0:
                    index.home_page()
                    choice_num_index = input("输入您选择的项目：")
                    if choice_num_index == "6":
                        ret_data = register.register_page()
                        register.register_user(ret_data[0],ret_data[1],ret_data[2],ret_data[3])
                        break
                    elif choice_num_index == "Q":
                        break
                    else:
                        break
                else:
                    break
            else:
                user_name = input("请输入您的账号名称：")
                password = input("请输入您的密码：")
                user_data["id"] = user_name
                user_data["pawd"] = password
                auth_data = loginpage.acc_auth(user_name, password)
        else:
            break


# index.home_page()
# choice_num_index = input("输入您选择的项目：")

from core import register
# if choice_num == 6:
#     core.register()

