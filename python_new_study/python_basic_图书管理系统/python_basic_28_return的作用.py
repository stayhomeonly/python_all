"""
#@Time：2022/7/17-16:54
#@file：python_basic_28_return的作用
#@Project:python_new_study
#@Content:

"""
"""
return 后面不执行
"""


def test01():
    print(122)
    return 123
    print("1234")


print(test01())  # return 后面的所有代码不执行
