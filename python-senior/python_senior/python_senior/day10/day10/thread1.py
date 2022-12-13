"""
主要是演示多线程与单线程的运行效率
进程  一个应用是由一个或者多个进程来实现的
线程  一个进程至少包含多个线程
对线程并发 就是由多个线程同时执行任务
"""
import time


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


start_time = time.time()
a()
b()
c()
end_time = time.time()
print(end_time - start_time)
