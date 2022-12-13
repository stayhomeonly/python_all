"""
#@Time：2022/12/6-20:47
#@file：python_basic_72(多个装饰器叠加使用)
#@Project:git_python
#@Content:

"""


def outer1(func1):
    def wrapper1(*args, **kwargs):
        print('开始执行outer1的wrapper')
        res = func1(*args, **kwargs)
        print('开始执行outer1的wrapper执行完毕')
        return res

    return wrapper1


def outer2(x):
    def outer(func2):
        def wrapper2(*args, **kwargs):
            print('开始执行outer2的wrapper')
            res = func2(*args, **kwargs) # fun2=outer.wrapper
            print('开始执行outer2的wrapper执行完毕')
            return res

        return wrapper2

    return outer


def outer3(func3):
    def wrapper3(*args, **kwargs):
        print('开始执行outer3的wrapper')
        res = func3(*args, **kwargs) #fun3=outer2.wrapper
        print('开始执行outer3的wrapper执行完毕')
        return res

    return wrapper3


# 多个装饰器叠加使用,执行代码outer1,再outer2，再outer3，实际上执行outer3最先执行，最后退出，然后
# outer
@outer3  # home=outer3(home)  outer3.wrapper(地址)
@outer2(10)  # outer=outer2(10) =>@outer => home=outer(home) outer2.wrapper(地址)
@outer1  # home=outer1(home)  outer1.wrapper(地址)
def home(z):
    print("执行home功能", z)

home(2)
# 开始执行outer3的wrapper
# 开始执行outer2的wrapper
# 开始执行outer1的wrapper
# 执行home功能 2
# 开始执行outer1的wrapper执行完毕
# 开始执行outer2的wrapper执行完毕
# 开始执行outer3的wrapper执行完毕


