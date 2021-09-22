# Author: ShiHang
import sys,os
print(sys.path)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_os=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path_os)
sys.path.append(path_os)
print(sys.path)