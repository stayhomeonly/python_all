# coding:utf-8
"""
#@Time：2022/11/12-20:01
#@file：python_basic_64(多进程，多线程)
#@Project:python_new_study
#@Content:

"""
'''
多进程：一个程序运行过程中，产生了多个了进程
n个正在运行的程序--至少n个进程
1个程序--可能只有一个进程，也可能有多个进程
'''

from multiprocessing import Process
import time

from time import process_time


# 引入进程类

def run1():
    print("执行了任务1！")
    time.sleep(5)


def run2():
    print("执行了任务2！")
    time.sleep(5)


def run3():
    print("执行了任务3！")
    time.sleep(5)


# 这是第一种，正常进行进程，从上而下
# start = time.time()
# run1()
# run2()
# run3()
# end = time.time()
# print("最终时间 ", end - start)

# 第二种多进程进行，互不干扰
P1 = Process(target=run1)  # (target=后面写上要执行的任务方法)
P2 = Process(target=run2)
P3 = Process(target=run3)

if __name__ == '__main__':

    P1.start()  # 启动进程,只能写到main函数下面

    P2.start()  # 启动进程

    P3.start()  # 启动进程

