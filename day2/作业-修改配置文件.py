# Author: ShiHang


# with open("hosts","r+") as f1:
#     # print(f1.read())
# with open("hosts", "r+") as f2:
#     # print(f2.read())
f1 = open("hosts","r+")
f2 = open("hosts.bak","w")

# print(f1.read())
code = "192.168.26.1"



for line in f1:
    print(line)
    if code in line:
        line = line.replace(code,"This is a test")
    f2.write(line)
f1.close()
f2.close()