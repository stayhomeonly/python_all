"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-10:06
知识点: 
---------------------------------
"""
"""
使用pytest参数化数据，让测试数据和测试逻辑分离
数据驱动：DDT(Data-driven testing)
        一般做接口自动化使用，使用数据的方式进行传参
关键字驱动：KDT(Keyword-driven testing)
        一般做UI自动化使用，它是将页面的某种行为、或固定的行为进行封装，封装后再进行传参。
        举个例子，比如我有一个网站，他有登录和注销，这个时候我把经常使用的登录封装好，以后就直接调用就行了。
"""
import pytest


def add(a, b):
    return a + b


print(add(1, 2))

cases = [{"parameter1": 1, "parameter2": 2, "result": 3},
         {"parameter1": 5, "parameter2": 7, "result": 12},
         {"parameter1": 6, "parameter2": 2, "result": 8},
         {"parameter1": 6, "parameter2": 2, "result": 9}]


# @pytest.mark.parametrize(变量名：str,数据源：list)  参数化测试用例，数据源列表中有多少个成员，测试用例就执行多少次
@pytest.mark.parametrize('case', cases) # 把cases中的每一个成员都赋值给case，每赋值一次，用例就会执行一次
def test_add(case):
    res = add(case["parameter1"], case["parameter2"])
    assert case["result"] == res


if __name__ == '__main__':
    pytest.main(["-vs", "./test_Parameter01.py"])
