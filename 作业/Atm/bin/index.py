# Auth: ShiHang


homepage=("欢迎来到小方银行".center(40,'-'),
       "1. 账户信息".center(40,' '),
       "2. 账户还款".center(40,' '),
       "3. 现金取款".center(40,' '),
       "4. 现金转账".center(40,' '),
       "5. 账单显示".center(40,' '),
       "6. 账号注册".center(40,' '),
       "7. 退出（输入Q）".center(40,' '),
)

def home_page():
    for line in homepage:
        print(line)
    return 0

