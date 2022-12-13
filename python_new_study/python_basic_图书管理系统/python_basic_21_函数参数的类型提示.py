"""
#@Time：2022/7/1-21:53
#@file：python_basic_21_函数参数的类型提示
#@Project:python_new_study
#@Content:

"""


def func(name, age):
    print(name)
    print(age)
    return 10


func(3.14, [1, 2, 3])


# 由于python是解释型的强类型动态语言，所以没有规定name,age必须是字符串和int

# python3.5之后，形参后面给了个提示功能，只要在后面在形参后面加上形参加上冒号即可
def func1(name: str, age: int = 88) -> int:  # 返回值也可以定义类型，可以提示调用的人，用-> 即可
    print(name)  # 如果想给，age设置一个默认值，直接在int=默认值
    print(age)
    return 10


print(func1.__annotations__)  # 函数的提示信息打印出来
