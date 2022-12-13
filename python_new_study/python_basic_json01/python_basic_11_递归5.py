"""
#@Time：2022/6/25-9:05
#@file：python_basic_11_递归1
#@Project:python_new_study
#@Content:

"""

s='abcd'
l=list(s)

def permutation(l,level):
    if level == len(l):
        print(l)
    for i in range(level,len(l)):
        l[level],l[i]=l[i], l[level]
        permutation(l,level+1)
        l[level], l[i] = l[i], l[level]


permutation(l, 0)


