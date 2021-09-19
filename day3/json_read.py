# Auth: ShiHang
import json



# f = open("test.txt",'r')
# # f.write(str(info))
# # data=eval(f.read())
# # print(data['age'])
# data=json.loads(f.read())
# print(data["age"])
# f.close()
import pickle
def func(name):
    print("ahah",name)
    print("hehe")
import pickle
f = open("test1.txt",'rb')
data1=pickle.loads(f)    #相当于data1=pickle.loads((f.read()))
print(data1["test"]("shihang"))