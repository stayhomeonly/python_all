"""
#@Time：2022/8/2-21:29
#@file：python_basic_41(九九乘法表)
#@Project:python_new_study
#@Content:

"""
# 九九乘法表
for j in range(1,10):
    for i in range(1,j+1):
        print(f'{j}*{i}={i*j}',end='\t')# \n表示换行，\t表示
    print('')