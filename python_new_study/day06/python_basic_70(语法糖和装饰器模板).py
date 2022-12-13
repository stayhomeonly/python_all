"""
#@Time：2022/11/30-20:33
#@file：python_basic_70(语法糖)
#@Project:git_python
#@Content:

"""

# 语法糖

import time


#
#
# def count_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         response = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return response
#
#     return wrapper
#
#
# @count_time  # 写了这个，等于写了这行代码inside=count_time(inside)
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
# #
# #
# print('原来inside的地址', inside('地方',5))
# #
#
# @count_time  # recharge=count_time(recharge)
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f"\r当前电量:{'■' * i} {i}%", end=' ')  # \r相当于回车
#     print('电量已经充满')
#
#     return 100
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         response = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return response
#
#     return wrapper
#
#
# inside('蓝色', s=3, z='炮车')
# recharge(23)


# 装饰器模板
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper


# def count_time(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# @count_time  # home=count_time(home)
# def home():
#     start = time.time()
#     time.sleep(2)
#     print("welcome")
#     end = time.time()
#     print(end - start)
#
#
# home()

def auth(func):
    # @wraps(func)  # 这个是wraps装饰器可以加，也可以不加，装饰器调用参数、属性、名字一致就行
    def wrapper(*args, **kwargs):
        """这是主页"""
        name = input('请输入账号>>>').strip()
        pwd = input('请输入密码>>>').strip()
        if name == 'jack' and pwd == '123':

            res = func(*args, **kwargs)
            return res

        else:
            print("账号和密码错误！")

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


@auth
def home():
    """这是主页"""
    time.sleep(2)
    print("welcome")


# home()
# home.__name__ = 原函数的内存地址.__name__  # __name__ 看函数的函数名的
# home.__doc__ = 原函数的内存地址.__doc__
# print(home.__name__)  # 如果不加上home.__name__='home'，打印出来
# # <function auth.<locals>.wrapper at 0x0000024BE02B7510>
# print(home.__doc__)
# print(home)  # <function home at 0x000001DCEF318510> 这是其实是wrapper的地址


# 直接通过参数传递
# 闭包函数
def g_outer(name, age):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(name, age)
            res = func(*args, **kwargs)
            return res

        return wrapper

    return outer


@g_outer('张大仙', 18)  # @outer,home=outer(home),home=wrapper
def home():
    """这是主页"""
    time.sleep(2)
    print("welcome")


@g_outer('张大仙', 20)
def index():
    pass
#

home()
index()
#
#
# # 有参装饰器的模板
# def g_outer(x):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
#     return outer

