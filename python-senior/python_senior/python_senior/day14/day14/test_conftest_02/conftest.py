"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-11:43
知识点: 
---------------------------------
"""
import pytest


@pytest.fixture(autouse=True)
def fun_scope():
    print("\r---------------------function自动执行之前---------------------")
    yield
    print("\r---------------------function自动执行之前---------------------")


@pytest.fixture(scope='class')
def class_scope():
    print("\r---------------------class自动执行之前---------------------")
    yield
    print("\r---------------------class自动执行之后---------------------")


@pytest.fixture(scope='module')
def module_scope():
    print("\r---------------------module自动执行之前---------------------")
    yield
    print("\r---------------------module自动执行之后---------------------")


@pytest.fixture(scope='session')
def session_scope():
    print("\r---------------------session自动执行之前---------------------")
    yield
    print("\r---------------------session自动执行之后---------------------")


@pytest.fixture(scope='package')
def package_scope():
    print("\r---------------------package自动执行之前---------------------")
    yield
    print("\r---------------------package自动执行之后---------------------")
