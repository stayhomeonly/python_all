"""
==================================
文件名: python03
作者:    Liu
时间:   2022/6/26-17:24
==================================
"""

"""
1.我们可以使用raise 自己触发异常  raise [Exception[,traceback]]
2.自定义异常:
    实际的工程项目中,我们有时候需要定义一个区别于系统的异常类,还好python为我们提供了一个可以自定义异常类的方法
"""


num = int(input("请输入您的分数:\n"))

if not (0 <= num <= 100):
    raise Exception("输入了无效的分数!")  # 主动抛异常
elif 0 <= num < 60:
    print('不及格')
else:
    print('及格')


# 自定义异常
class NotValidNumberError(Exception):  # 异常类必须继承Exception类
    pass


num = int(input("请输入您的分数:\n"))

if not (0 <= num <= 100):
    raise NotValidNumberError("输入了无效的分数!")  # 主动抛异常
elif 0 <= num < 60:
    print('不及格')
else:
    print('及格')
