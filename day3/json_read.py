# Auth: ShiHang
import json


f = open("test.txt",'r')
# f.write(str(info))
# data=eval(f.read())
# print(data['age'])
data=json.loads(f.read())
print(data["age"])
f.close()