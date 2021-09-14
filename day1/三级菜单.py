# Author: ShiHang
linux_disk = {
    "bin":{
        "sbin":['find','ls','ifconfig','netstat'],
        "usr":['log','file','test']
    },
    "var":{
        "log":['messages','contain','systemd']
    },
    "dev":{
        "vda":['vda1','vda2','vda3']
    },
    "home":{
        "shihang":['shell','log','bin']
    },
}

# print(linux_disk)
# print(linux_disk["bin"]["sbin"][1])
# linux_disk.setdefault("media",{"package":[1,2,3]})
# print(linux_disk)
#去字典里取media的值，如果存在，则返回，如果不在则插入
exit_flag = False
while not exit_flag:
    print("--------------")
    print("Linux 一级菜单：")
    for index,i in enumerate(linux_disk):
        print(index,i)
    dir_name1 = input("选择你要查看的二级菜单,退出请输入Q ：")
    if dir_name1 in linux_disk:
        while not exit_flag:
            print("--------------")
            print("Linux 二级菜单：")
            for index,i in enumerate(linux_disk[dir_name1]):
                print(index,i)
            dir_name2 = input("选择你要查看的文件：")
            if dir_name2 in linux_disk[dir_name1]:
                while not exit_flag:
                    print("--------------")
                    print("Linux 文件菜单：")
                    for index, i in enumerate(linux_disk[dir_name1][dir_name2]):
                        print(index, i)
                    choice = input("是否要继续查看，返回：B，继续：Y，退出：Q")
                    if choice in linux_disk[dir_name1][dir_name2]:
                        dir_name3 = input("选择你要查看的文件内容：")
                        if dir_name3 in linux_disk[dir_name1][dir_name2]:
                            print(dir_name3)
                        else:
                            break
                    elif choice == "Y":
                        pass
                    elif choice == "Q":
                        exit_flag = True
                    elif choice == "B":
                        break
                    else:
                        print("3:输入错误，请重新输入！")
            elif dir_name2 == "Q":
                exit_flag = True
            else:
                print("2:输入错误，请重新输入！")
    elif dir_name1 == "Q":
        exit_flag = True
    else:
        print("1:输入错误，请重新输入！")