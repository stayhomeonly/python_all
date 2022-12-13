"""
#@Time：2022/12/7-20:36
#@file：python_basic_73(迭代器)
#@Project:git_python
#@Content:

"""
# 迭代器：不依赖于索引的取值方式
# 可迭代对象：可以转换为迭代器的对象，就称之为可迭代对象
# 只要内置有__iter__()方法的就可以称之为可迭代对象
l = [1, 2, 3]
# l.__iter__()
s = '张大仙'
# s.__iter__()
t = (1, 2, 3)
# t.__iter__()
# d={'key1':'1'}
# d.__iter__()
s1 = {1, 2, 3}
# s1.__iter__()


d1 = {'key1': 1, 'key2': 2, 'key3': 3}
res = d1.__iter__()  # 调用__inter__就是可以把无索引的转变成迭代器，可迭代
print(res)

# print(res.__next__())  # __next__能够拿到key值
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# 不依赖索引取值
while True:
    try:
        print(res.__next__())
    except StopIteration as e:
        break

# 迭代器对象：内置有__next__方法，并且还有__iter__()方法的对象
# 迭代器对象调用：__next__()方法，就会得到迭代器的下一个值
# 迭代器对象调用__iter__()方法,得到的是迭代器本身（和没调一样）
d={1,2,3}
# 1、调用对象的__iter__()方法，得到一个它的迭代器版本
# 2、调用迭代器的__next__()方法，拿到一个返回值，就赋值给key
# 3、循环执行第二步，直到抛出异常，就捕获异常，并结束循环
for key in d:
    print(key)