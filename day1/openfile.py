# # Author: ShiHang
# f = open("product.txt","r+",encoding="utf-8") #读写最多用为r+模式，w+和a+不常用
# f = open("product.txt","w+",encoding="utf-8") #写读
# f = open("product.txt","a+",encoding="utf-8") #追加读写
# f = open("product.txt","rb")
f = open("product.txt","wb")#二进制格式写文件，网络传输
# # print(f.read())
# # print(a)
# # print(f.encoding)
# f.write("\nHello World!\n")
# f.truncate(10)

#修改
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# # f.write("\n--------------\n")    #对源文件修改，则会进行覆盖原文中相同字节的东西
# f.seek(0)
# print(f.tell())
# print(f.readline())
f.write("\n------222-------\n".encode())
# print(f.readline())





