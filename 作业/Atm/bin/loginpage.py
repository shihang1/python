# Auth: ShiHang
import os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
loginepage=("欢迎来到小方银行".center(40,'-'),
          "1. 登录账号".center(40,' '),
          "2. 注册账号".center(40,' '),
          "3. 忘记密码".center(40,' '),
          )
def login_in():
    for line in loginepage:
        print(line)
    return 0

def acc_auth(name,passwd):
    file_path = "%s/db/account" %BASE_DIR
    file_name = "%s/%s.json" %(file_path,name)
    # print(file_name)
    if os.path.isfile(file_name):
        with open(file_name,'r') as f:
            account_data = eval(f.read())
            if account_data['password'] == str(passwd):
                print("密码输入正确！")
                return 0
            else:
                print("密码输入错误")
                return -1
    else:
        print("账号不存在！")
        return  -1
acc_auth("shihang",123456)

