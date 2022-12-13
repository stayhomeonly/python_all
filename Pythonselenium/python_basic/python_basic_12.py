"""
#@Time：2022/5/31-16:40
#@file：python_basic_12
#@Project:git_python
#@Content:

"""
# 需求，写一个函数显示充电的进度条
import time
def rechange(num):
    for i in range(num,101):

        time.sleep(1)
        print(f'\r当前电量为：{"■"*i} {i}%',end=' ') # \r是回车的操作。即光标会移动到初始的位置，并且覆盖掉之前的内容。
    print('电量已经充满')
rechange(20)