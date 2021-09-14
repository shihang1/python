# Author: ShiHang
linux_disk = {
    "bin":{
        "sbin":['find','ls','ifconfig','netstat']
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

for i in linux_disk:
    print(i,linux_disk[i])
print('-'.center(20,'-'))
for i,k in linux_disk.items():
    print(i,k)