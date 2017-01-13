#Copyright (c) 2017, BaoXingce.
#E-mail: 1652256031@qq.com
#License: GPL
import sys
import time
time.sleep(3)

sys.path.append("C:\\Program Files\\Anaconda3\\Lib\\site-packages")
from condition import *
from imgSearch import *
def success():
    print("succeed")
def failure():
    print("failed")
begin = time.time()
test=condition(success,failure,dotCmp((777,231),(225,183,193),0.15))
test.execute()
end = time.time()
print (end-begin)
begin = time.time()
test2=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3))
test2.execute()
end = time.time()
print (end-begin)
begin = time.time()
test3=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3,method=histgram(split=True)))
test3.execute()
end = time.time()
print (end-begin)
begin = time.time()
test4=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3,method=dHash()))
test4.execute()
end = time.time()
print (end-begin)
begin = time.time()
test5=condition(success,failure,imgCmp(((283,61),(1082,660)),"C:\\Users\\bxc\\Desktop\\website\\PDF\\picture\\2.jpeg",0.3,method=pixelCompare()))
test5.execute()
end = time.time()
print (end-begin)
begin = time.time()
list1=imgSearch("E:\\1.jpg").averagePosition()
#print (len(list1))
print (list1)
end = time.time()
print (end-begin)
