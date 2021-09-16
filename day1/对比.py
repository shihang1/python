# Author: ShiHang
num_list = [2,3,5,32,445,2323,234]

print(num_list)
print(num_list[1])
maxnum=num_list[0]

for n in num_list:
    if n > maxnum:
        maxnum=n
print(maxnum)