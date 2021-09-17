# Author: ShiHang
name="a"
passwd="b"

def func1(ags):
    def func3(item):
        def func2(*args,**kwargs):
            name1 = input("请输入你的用户名：").strip()
            passwd1 = input("请输入你的密码：").strip()
            if ags == "local":
                # name1 = input("请输入你的用户名：").strip()
                # passwd1 = input("请输入你的密码：").strip()
                if name1 == name and passwd1 == passwd:
                    print("输入正确！")
                    item(*args,**kwargs)
                else:
                    print("输入错误！")
            elif ags == "file":
                print("选择其它方式！")
        return func2
    return func3

def index():
    print("Welcome to index!")
@func1(ags="local")
def home():
    print("Welcome to HOME page!")
@func1(ags="file")
def media():
    print("Welcome to MEDIA page!")

index()
home()
media()


