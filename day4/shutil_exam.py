# Author: ShiHang
import shutil
# 高级的文件、文件夹、压缩包处理模块

# f1 = open("testfile.txt",encoding='utf-8')
#
# f2 = open("testfile1.txt",'w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)   #文件拷贝


shutil.copyfile("testfile.txt","testfile2.txt")   #文件拷贝


# shutil.copymode(src,dest)
# 仅拷贝权限，内容、组、用户不变

# shutil.copystat(src,dest)
# 拷贝文件所有信息