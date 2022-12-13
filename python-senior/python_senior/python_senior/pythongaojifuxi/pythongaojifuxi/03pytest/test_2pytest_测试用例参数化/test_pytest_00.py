"""
pytest 参数化
"""
import pytest

cases = [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.parametrize("c", cases)  # 参数化：声明使用 cases中的数据
def test_add(c):
    print(c)


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest_00.py'])
