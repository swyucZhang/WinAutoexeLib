import sys
import time
time.sleep(3)

sys.path.append("C:\\Program Files\\Anaconda3\\Lib\\site-packages")
from condition import *

def success():
    print("succeed")
def failure():
    print("failed")
test=condition(success,failure,dotCmp((777,231),(225,183,193),0.15))
test.execute()
test2=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3))
test2.execute()
test3=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3,method=histgram(split=True)))
test3.execute()
test4=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3,method=dHash()))
test4.execute()
test5=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3,method=pixelCompare()))
test5.execute()
