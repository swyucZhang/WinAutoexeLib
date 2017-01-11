import sys
#main.py

sys.path.append("C:\\Program Files\\Anaconda3\\Lib\\site-packages")
from condition import *

def success():
    print("succeed")
def failure():
    print("failed")
test=condition(success,failure,dotCmp((777,231),(227,185,195),3))
test.execute()
