"""
#@Time：2022/12/10-20:39
#@file：python_basic_74(生成器)
#@Project:git_python
#@Content:

"""
# 生成器
def func():
    print("第一次执行")
    yield 1  # 和return最大区别，return执行完了之后后面就不会执行了，yield则不会
    print("第二次执行")
    yield 2
    print("第三次执行")
    yield 3
    print("第四次执行")

res=func()
print(res)
res.__iter__() # 相当于iter(res)
print(res.__next__()) #相当于next(res)
print(res.__next__())
print(res.__next__())
print(res.__next__())


# 生成器就是迭代器
