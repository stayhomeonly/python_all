"""
#@Time：2022/11/27-18:55
#@file：python_basic_68(闭包函数)
#@Project:git_python
#@Content:

"""


# 闭包函数
# 闭函数：闭 封闭的意思，函数被封闭起来
# 包函数：函数内部包含对外层函数作用域名字的引用
def f1(x):
    def f2():
        print(x)

    return f2  # 记住一定不要加括号，加括号就是返回值，不加就是返回内存地址


res = f1(10)
print(res)  # <function f1.<locals>.f2 at 0x0000020B0F5E7E18>
res()


