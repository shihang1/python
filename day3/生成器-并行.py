# Auth: ShiHang
import time
def custom(name):
    print("%s is coming!" %name)
    while True:
        who = yield
        print("球星【%s】来了！，%s找他签名" %(who,name))
# c =custom("shihang")
# c.__next__()
# c.send("haha")
# c.__next__()__next__
# c.send('hehe')
def prducer():
    a=custom("shihang")
    b=custom("fangming")
    a.__next__()
    b.__next__()
    for i in range(5):
        time.sleep(1)
        a.send(i)
        b.send(i)
        print("------------")
prducer()