"""
#@Time：2023/1/1-21:51
#@file：python_basic_81(递归用例)
#@Project:git_python1
#@Content:

"""
# 要求：下面列表的每一个值单独打印出来
l = [1, 2, [3, [4, [5, [6, [7, [8, [9, [10, [11, 12]]]]]]]]]]


l1 = [1, 2, [3, 4]]
#如果关于l1想把里面的值全部打印出来
for i in l1:
    if type(i) is list:
        for j in i:
            if type(j) is list: #如果想把l1里面的值全部出来，如果有两层，就要多嵌套if语句，
                # 但是如果不清楚有多少层list,所以要用到递归
                pass
            else:
                print(j)
    else:
        print(i)

def func(li):
    for i in li:
        if type(i) is list:
            func(i)  # 如何分析这段代码，因为就是不清楚里面有多少层，不能一直写if语句，所以问递归
            # 用递归就要用函数，所以要定义func

        else:
            print(i)


func(l)
