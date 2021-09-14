# Author: ShiHang

name = input("名字：")
#python2 raw_input
#python3  input
age = int (input("年龄："))
print (type(age),type(str(age)))
job = input("工作：")

info = '''
--------info of %s ---------
name: %s
age: %d
job: %s
''' %(name,name,age,job)
print(info)

info2 = '''
--------info of {_name} ---------
name: {_name}
age: {_age}
job: {_job}
'''.format(_name=name,
           _age=age,
           _job=job)
print(info2)

info3 = '''
--------info of {0} ---------
name: {0}
age: {1}
job: {2}
'''.format(name,age,job)
print(info3)