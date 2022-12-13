"""
#@Time：2022/12/9-17:03
#@file：装饰器写法
#@Project:git_python
#@Content:

"""

"""
def start_test():
    print("测试已经开始")
    print("执行用例")
    print("执行用例结束")
"""
import time

# 需求：现在需要给这个函数start_test加一个计时的功能
# 第一种方案

# def start_test():
#     start_time = time.time()
#     time.sleep(2)
#
#     print("测试已经开始")
#     print("执行用例")
#     print("执行用例结束")
#     end_time = time.time()
#     print(end_time - start_time)
#
#
# start_test()
'''
第一种方案实现了功能，但是改变了源代码，如果该函数已经被调用，那么就会被影响
'''

# 第二种方案
# def start_test():
#     print("测试已经开始")
#     print("执行用例")
#     print("执行用例结束")
#
#
# def count_time():
#     start_time = time.time()
#     start_test()
#     time.sleep(2)
#     end_time = time.time()
#     print(end_time - start_time)
#
#
# count_time()

'''
第二种方案，没有改变源代码，但是改变了调用方式，所以不合格
'''


# 第三种方案
# def start_test(s):
#     print(f"测试已经开始{s}")
#     print("执行用例")
#     print("执行用例结束")
#
#
# # def count_time(func):
# #     start_time = time.time()
# #     func()  #如果这样写死，显得自己不专业，可以用传参的方式,但是如果需要传入参数就不能这样写
# #     time.sleep(2)
# #     end_time = time.time()
# #     print(end_time - start_time)
# def count_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)  # 如果这样写死，显得自己不专业，可以用传参的方式,但是如果需要传入参数就不能这样写
#         time.sleep(2)
#         end_time = time.time()
#         print(end_time - start_time)
#
#         return res
#
#     return wrapper
#
#
# start_test=count_time(start_test)
# start_test(2)

"""
最终方案
"""

def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)  # 如果这样写死，显得自己不专业，可以用传参的方式,但是如果需要传入参数就不能这样写
        time.sleep(2)
        end_time = time.time()
        print(end_time - start_time)

        return res

    return wrapper
@count_time
def start_test(s):
    print(f"测试已经开始{s}")
    print("执行用例")
    print("执行用例结束")

start_test(2)