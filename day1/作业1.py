# Author: ShiHang
#购物车优化
#用户入口  1.商品信息存在文件里  2.已购买商品，余额记录
#商家入口  1.可以添加商品  2.修改商品价格
product_all = []
product_file_name = "product.txt"
with open(product_file_name,encoding='utf-8') as product_list:
    for item in product_list:
        product_all.append(item.strip())
    print(product_all)
