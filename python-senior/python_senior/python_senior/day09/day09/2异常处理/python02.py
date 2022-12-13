"""
==================================
文件名: python02
作者:    Liu
时间:   2022/6/26-17:02
==================================
"""
"""
异常的处理

try:
    语句块1
except 异常类型1:
    语句块2
except 异常类型2:
    语句块3
....
[else:] else是可选的,如果语句块1没有异常,则执行else的内容
[finally:] finally为可选内容,不管有没有异常,最后都会执行

执行try中的语句块1,如果语句块1出现了异常类型1,则执行语句块2...
"""

try:
    num = int(input("请输入整数类型的数字:\n"))

    if num % 2 == 0:
        print('%s是偶数' % num)
    else:
        print('{}是奇数'.format(num))
except ValueError:  # 如果try中的代码出现了ValueError,则执行except下的代码
    print('请输入正确的整数!')
else:
    print('没出现异常!')  # 如果try中的代码没有出现异常,则执行else下的代码
finally:
    print('程序执行完成~')  # 不管try中的代码有没有异常,最终都会执行

"""分别处理多种异常"""

try:
    num = int(input("请输入一个整数:\n"))
    print(100 / num)
except ValueError:
    print('请输入正确的数据!')
except ZeroDivisionError:
    print('除数不能为0！')

"""同时处理多种异常"""

try:
    num = int(input("请输入一个整数:\n"))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('请输入正确的数据!')

"""万能处理异常的方式"""

try:
    num = int(input("请输入一个整数:\n"))
    print(100 / num)
except Exception as e:  # 如果出现异常,就执行except下的代码
    print('请输入正确的数据!', e)  # e代表报错信息
