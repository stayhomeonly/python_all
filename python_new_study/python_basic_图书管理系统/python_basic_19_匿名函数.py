"""
#@Time：2022/6/29-20:58
#@file：python_basic_19_匿名函数
#@Project:python_new_study
#@Content:

"""


# 有名函数(需要重复调用)
def func(x, y):
    return x + y


# 匿名函数(临时调用一次)
# res=(lambda x, y=1: x + y)(1,2)
# print(res)


# lambda x, y=1: x + y

info = {
    'jack': 5000,
    'tony': 2500,
    'andy': 8000,
    'amy': 6000,
    'lucy': 11000,
}
# 找出字典里面薪资最高的人
res = max(info)  # tony ,比的是键，键是字符串，按照ascic表来比的
print(res)


def func(key):
    return info[key]


res1 = max(info, key=func)  # 这里不能用func(),不然就是调用函数，我们只是需要一个内存地址
print(res1)
# 用匿名函数的写法
res2 = max(info, key=lambda key: info[key])
print(res2)

l = [3, 1, 4, 5, 9, 2, 6]
l.sort(reverse=True)  # 降序
print(l)

l = [(1, 2), (3, 4), (2, 1), (4, 3)]
# 把l按照索引1号位从小到大排序
for i in range(len(l) - 1):
    for j in range(len(l) - 1):

        if l[j][1] > l[j + 1][1]:
            l[j], l[j + 1] = l[j + 1], l[j]

        else:
            pass

print(l)


# 另外一个写法
def takeSecond(item):
    return item[1]


# 第一种写法
l.sort(key=takeSecond)  # takeSecond代表着内存地址
print(l)
# 第二种写法
l.sort(key=lambda item: item[1])  # 下标为1,排序
print(l)

# 把列表中的每个元素加上_老坛酸菜
l = ['康师傅', '统一', '大今野', '白象']
new_l = [name + "_老坛酸菜" for name in l]  # 用的是列表生成器
print(new_l)

res = map(lambda name: name + "_老坛酸菜", l)  # map每迭代一次，就会把值传给l
print(res)  # res就是一个生成器
print(res.__next__())
