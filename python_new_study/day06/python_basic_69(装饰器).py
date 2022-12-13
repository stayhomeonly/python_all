"""
#@Time：2022/11/28-20:27
#@file：python_basic_69(装饰器)
#@Project:git_python
#@Content:

"""
# 装饰器
# 器：器具、工具
# 装饰：为其他事务添加额外的功能
# 定义一个函数（不规范），这个函数的功能是来装饰其他函数
# 也就是说为其它函数增加额外的功能的

# 开放封闭原则
# 开放：对扩展功能（增加功能）开放，扩展功能的意思是在源代码不做任何改变的情况增加功能
# 封闭：对修改源代码是封闭的

# 装饰器：不修改被装饰对象的源代码，也不修改调用方式的前提下，给被装饰对象添加新的功能
import time


# 方案一：
# 问题；没有修改调用方式，但是修改了源代码
# def inside(group, s):
#     start=time.time()
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#     end=time.time()
#     print(end - start)
#
#
# inside('红色', 5)


# 方案二
# 问题：
# 现在没有改变他的源码，也没有改变调用方式，但是这个函数每次调用的时候，都需要
# 写重复的代码，这是一种非常low行为
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# start = time.time()
# inside('红色', 5)
# end = time.time()
# print(end - start)


# 方案三：
# 问题：解决方案二的冗余的问题也没有修改装饰对象的代码，同时还为其他增加了功能
# 但是被装饰对象的调用方式被修改了
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# def wrapper():
#     start = time.time()
#     inside('红色', 5)
#     end = time.time()
#     print(end - start)
#
#
# wrapper()

# 方案四


# def inside(group, s,z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# def wrapper(*args,**kwargs):
#     start = time.time()
#     inside(*args,**kwargs)
#     end = time.time()
#     print(end - start)


# 方案五
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# print('原来inside的地址', inside)
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#
#     return wrapper
#
#
# inside = outer(inside)  # 这里用inside作为变量名，就是为了偷梁换柱，
# print("现在inside的地", inside)
# inside('蓝色', s=3, z='炮车')

# 方案六
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# print('原来inside的地址', inside)


# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f"\r当前电量:{'■' * i} {i}%", end=' ')  # \r相当于回车
#     print('电量已经充满')
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#
#     return wrapper
#
#
# recharge=outer(recharge)
# recharge(20)

#
#
# inside = outer(inside)  # 这里用inside作为变量名，就是为了偷梁换柱，
# print("现在inside的地", inside)
# inside('蓝色', s=3, z='炮车')

# 方案七
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}方正营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#
#
# print('原来inside的地址', inside)


def recharge(num):
    for i in range(num, 101):
        time.sleep(0.05)
        print(f"\r当前电量:{'■' * i} {i}%", end=' ')  # \r相当于回车
    print('电量已经充满')

    return 100


def outer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return response

    return wrapper


recharge = outer(recharge)  # 如果recharge返回值也是需要的，就要在调用的加一个返回值，最后返回返回值
res = recharge(20)
print(res)

#
#
# inside = outer(inside)  # 这里用inside作为变量名，就是为了偷梁换柱，
# print("现在inside的地", inside)
# inside('蓝色', s=3, z='炮车')
