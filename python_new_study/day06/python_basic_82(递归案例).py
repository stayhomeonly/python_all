"""
#@Time：2023/1/1-22:04
#@file：python_basic_82(递归案例)
#@Project:git_python1
#@Content:

"""
# 二 要求：把下列的字符串全排列
s = 'abcd'

l = list(s)


def permutation(l, level):
    if level == len(l):
        print(l)
    for i in range(level, len(l)):
        l[level], l[i] = l[i], l[level]
        permutation(l, level + 1)
        l[level], l[i] = l[i], l[level]



permutation(l, 0)
# 可以看一下全排列算法的图

