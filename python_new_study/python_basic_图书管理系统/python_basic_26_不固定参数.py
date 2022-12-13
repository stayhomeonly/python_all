"""
#@Time：2022/7/13-21:16
#@file：python_basic_26_不固定参数
#@Project:python_new_study
#@Content:

"""


def stu(name: str, age: int, *args, **kwargs: dict):  # *args会把多余的元素自动组成一个元祖
    print(name, age, args, kwargs)
    print(kwargs.get('add')) #就算没有这个键也不会报错


stu("fengxin", 25, "man", add="jiangsu")  # fengxin 25 ('man',) {'add': 'jiangsu'}
