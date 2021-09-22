# Author: ShiHang
# 1、时间戳
# 2、struct_time(tuple)
# 3、格式化字符串

import time
print(time.time())  #获取时间戳
print(time.localtime())  #转换时间戳为struct_time(tuple)，UTC时区
print(time.timezone/3600)  #东八区
print(time.daylight)
# time.sleep(2)
print(time.gmtime())
print(time.gmtime(100000000))
print(time.gmtime(time.time()))  #转换时间戳为struct_time(tuple)，本地时间,UTC+8时区
time_1=time.localtime()
print(time_1.tm_year,time_1.tm_mon,time_1.tm_mday)
print(time.mktime(time_1))    #元组转换成时间戳
time_2=time.strftime("%Y-%m-%d %H:%M:%S",time_1)  #将时间戳按照特定格式输出，元组----》格式化的字符串
print(time_2)

print(time.strptime('2021-09-22 16:09:23',"%Y-%m-%d %H:%M:%S"))
print(time.strptime('2021-09-22 16:09:23',"%Y-%m-%S %H:%M:%d"))

print(time.asctime(time_1))  #接受的元组数据

print(time.ctime())   #接受的是时间戳数据

print("分隔符".center(50,'-'))

import datetime
print(datetime.datetime.now())   #当前时间
print((datetime.date.fromtimestamp((time.time()))))  #时间戳转换日期格式  yyyy-mm-dd
print(datetime.datetime.now() + datetime.timedelta(3))  #当前时间加3天
print(datetime.datetime.now() + datetime.timedelta(-3))  #当前时间减3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  #当前时间+30分钟

