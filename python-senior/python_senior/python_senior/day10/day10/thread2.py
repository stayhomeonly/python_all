import time
import threading

import os

def a():
    print('我是第一方法')
    time.sleep(10)
    print('第一个方法结束了')


def b():
    print('我是第二方法')
    time.sleep(10)
    print('第二个方法结束了')


def c():
    print('我是第三方法')
    time.sleep(10)
    print('第三个方法结束了')


# start_time = time.time()
t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)
t3 = threading.Thread(target=c)
print("*****************")

t1.start()
t2.start()
t3.start()
# end_time = time.time()
# print(end_time - start_time)
