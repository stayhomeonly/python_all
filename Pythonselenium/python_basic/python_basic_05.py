"""
#@Time：2022/5/21-20:00
#@file：python_basic_05
#@Project:python_basic05.py
#@Content:

"""
'''
*
**
***
****
*****
****
***
**
*

'''
# 用*键打印上图一个直角三角形
for i in range(10):
    if i <= 5:
        print("*" * i)
    else:
        print((10 - i) * '*')
# 用一个*键打印出四行五星的矩形
for n in range(4):
    for i in range(5):
        print('*', end='')  # 加了end才可以不换行
    print()  # 这个是为了控制程序打印完5个*之后换行

# 打印一个直角三角形
for m in range(4):  # 外循环4次
    for i in range(m + 1):  # 内循环
        print('*', end='')
    print()


# 栈：用来存放变量名，堆：用来存放具体值




# 打印9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()

