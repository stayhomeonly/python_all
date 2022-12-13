# coding:utf-8
"""
#@Time：2022/11/12-20:24
#@file：python_basic_65(多线程)
#@Project:python_new_study
#@Content:

"""
'''
线程是CPU调度的基本单位，是进程中具体的执行单元
进程包含线程，一个进程中至少包含一个线程；
如果一个进程中包含了多个线程，称为多线程
'''

import threading
import time


def run(name):
    print("执行任务1")
    time.sleep(5)


# 程序执行时，程序本身就是一个线程，称为主线程
# 手动创建的线程，称为子线程
# 主线程执行过程中并不会等待子线程执行完毕，会直接执行后面剩余的代码

# 创建线程对象
t1 = threading.Thread(target=run, args=("t1",))  # 加了参数name,就要写args

t2 = threading.Thread(target=run, args=("t2",))

t3 = threading.Thread(target=run, args=("t3",))
start_time = time.time()
# 启动线程
t1.start()
t2.start()
t3.start()
end_time = time.time()
print('多线程总耗时:{}'.format(end_time - start_time))
# 为什么有多进程，还要用多线程
# 因为在多进程切换消耗的CPU资源比较多

# t1.join()  # 需要等待当前线程执行完毕，才能继续执行主线程
# t2.join()
# t3.join()

print("执行完毕！")
