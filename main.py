import sys


sys.path.append("C:\\Program Files\\Anaconda3\\Lib\\site-packages")
from condition import *

def success():
    print("succeed")
def failure():
    print("failed")
test=condition(success,failure,dotCmp((777,231),(225,183,193),50))
test.execute()
test2=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.4))
test2.execute()
