"""
#@Time：2022/12/16-16:16
#@file：python(yield)
#@Project:git_python1
#@Content:

"""


def fun1():
    while True:
        res = yield 1
        print(res)


res1 = fun1()
print(next(res1))  # 第一步是1,相当于调用了代码
print(next(res1))  # 第二步就会返回None,在返回1
print(res1.send(10)) #第三步10赋值给yield,返回yield ,也就是10
