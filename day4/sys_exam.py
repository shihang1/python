# Author: ShiHang
import sys_exam,os
print(sys_exam.path)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_os=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path_os)
sys_exam.path.append(path_os)
print(sys_exam.path)