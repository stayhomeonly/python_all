"""
-------------------------------------------------
   date      :2021/11/8-10:31
   Author    :Lee
   File Name :test_ddt01
-------------------------------------------------
"""

"""
使用 pytest参数化数据，让测试数据和测试逻辑分离。
"""

import pytest


def add(a, b):
    return a + b


cases = [{"params1": 10, "params2": 20, "exp": 30},
         {"params1": 15, "params2": 25, "exp": 40},
         {"params1": -10, "params2": 20, "exp": 10},
         {"params1": -10, "params2": -20, "exp": -30},
         {"params1": -10, "params2": -10, "exp": -20}
         ]


@pytest.mark.parametrize("case", cases)
def test_add(case):  # {"params1": -10, "params2": 20, "exp": 10}
    res = add(case['params1'], case['params2'])
    assert case['exp'] == res


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest_01.py'])
