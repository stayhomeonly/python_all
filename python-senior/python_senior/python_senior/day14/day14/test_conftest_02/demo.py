"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-12:01
知识点: 
---------------------------------
"""


def a():
    b = [1, 2, 3, 4, 5, 6]
    for i in b:
        yield i


b = a()
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())  # StopIteration 当值取完之后，再迭代时会报错,可以通过捕捉这个异常来判断是否还有值
