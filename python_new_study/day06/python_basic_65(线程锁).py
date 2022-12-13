# coding:utf-8
"""
#@Time：2022/11/16-20:41
#@file：python_basic_65(线程锁)
#@Project:python_new_study
#@Content:

"""
import threading

'''
线程锁（互斥锁）：当一个线程设置上锁之后，就必须等到这个锁释放之后才能调度其他的线程
1：创建一个锁的对象
'''
lock = threading.Lock()  # 创建锁
lock.acquire()  # 设置锁

number = 100


def run(name):
    global number  # 如果不设置成全局变量，num就会一直显示num=99
    number = number - 1
    lock.acquire()  # 设置锁
    print('线程', name, '执行了,目前num的值为：', number)
    lock.release()  # 释放锁


for i in range(1, 101):
    t = threading.Thread(target=run, args=(i,))
    t.start()
