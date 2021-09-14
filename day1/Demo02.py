# Author: ShiHang
all_name = [["shihang",5000],["fangming",10000]]
products = [["香烟",50],["红酒",100],["自行车",800],["神仙水",1500],["茅台白酒",3000]]
shopping_list = []
name = input("请输入您的账号：")
num = 0
while num < len(all_name):
    print("-------商品列表--------")
    for index, item in enumerate(products):
        print(index, item)
    print("---------------------")
    for i in all_name:
        if name == all_name[num][0]:
            salary = all_name[num][1]
            print("您的余额还有：",salary)
            while True:
                product_num = input("输入您想购买的商品：")
                if product_num.isdigit():
                    product_num = int(product_num)
                    if product_num < len(products) and product_num >= 0:
                        if salary < products[product_num][1]:
                            print("余额不足，请重新选择！")
                        else:
                            salary -= products[product_num][1]
                            print("---------------------")
                            print("您购买的商品是：",products[product_num][0])
                            print("消费的金额是：",products[product_num][1],"元","余额：",salary)
                    else:
                        print("您输入的商品号不在列表中！")
                else:
                    print("输入的商品号码不对！")

        else:
            num +=1
    else:
        print("账号输入错误，请重新输入！")
        name = input("请输入您的账号：")
        num = 0
