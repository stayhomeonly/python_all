"""
==================================
文件名: python01
作者:    Liu
时间:   2022/6/26-16:49
==================================
"""

"""
错误和异常的区别:
错误: 不能通过解释器的编译,这种叫错误
异常: 编译通过,运行时出现问题叫异常
"""

# 常见的错误
#  print("Hello World")  # 缩进错误 IndentationError: unexpected indent
# print("Hello World"  # 语法错误  SyntaxError: unexpected EOF while parsing

# 常见的异常
# print(10/0)  # 除0异常 ZeroDivisionError: division by zero
# list1 = [1, 2, 3, 4]
# print(list1[4])  # 下标越界异常 IndexError: list index out of range

num = int(input("请输入一个整数:\n"))
print(100 / num)
