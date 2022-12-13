"""
================================
  Author   :  Lee
  FileName :  conftest.py
  Date     :  2022/8/8 - 16:42
================================
"""
import pytest


# @pytest.fixture(scope='function',autouse=True)  # 在每个测试方法执行前和执行后自动执行
# def func_scope():
#     print('测试方法执行前----')
#     yield
#     print('测试方法执行后----')


#
# @pytest.fixture(scope='class',autouse=True)
# def class_scope():
#     print('--class前--')
#     yield
#     print('--class后--')
#
#
# @pytest.fixture(scope='module', autouse=True)  # 如果声明了autouse=True参数就会在当前模块执行前后自动使用
# def module_scope():
#     print('----conftest-------module前执行-----------')
#     yield
#     print('----conftest-------module后执行-----------')
