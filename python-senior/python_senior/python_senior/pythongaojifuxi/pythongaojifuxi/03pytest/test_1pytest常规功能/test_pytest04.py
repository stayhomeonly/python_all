"""
============================
1/ 使用场景
在日常功能测试用例非常多时，比如有1千条用例，假设每个用例执行需要1分钟，如果单个测试人员执行需要1000分钟才能跑完
当项目非常紧急时，会需要协调多个测试资源来把任务分成两部分，于是执行时间缩短一半，如果有10个小伙伴，那么执行时间就会变成十分之一，大大节省了测试时间
为了节省项目测试时间，10个测试同时并行测试，这就是分布式执行
同样道理，当我们自动化测试用例非常多的时候， 一条条按顺序执行会非常慢，pytest-xdist的出现就是为了让自动化测试用例可以分布式执行，从而大大节省自动化测试执行的时间
pytest-xdist是属于进程级别的并发
分布式执行用例的设计原则（重点）
当然自动化测试用例要想能够分布式执行，还是要满足一些条件的：
2/分布式执行用例的设计原则（重点）
用例之间相互独立：保证用例之间没有依赖关系，用例可以完全独立运行
用例没有执行顺序：保证随机顺序的执行用例都可正常执行
用例之间互不影响：保证用例的运行结果不会影响到其他用例
3/ pip install pytest-xdist
   pytest -s -n 2(auto 自动检测cpu核数，最大量并发)

====失败重跑

1、安装插件: pip3 install pytest-rerunfailures
在pytest.ini文件中添加: addopts = -vs --reruns=5 --reruns-delay=3
--reruns n（重新运行次数），--reruns-delay m（等待运行秒数）
=============================
"""

import pytest, requests


class TestLogin:
    # 登录成功
    def test_login01(self):
        assert 1 == 2

    # 用户名错误
    def test_login02(self):
        assert "H" in "Hello World"

    def test_login03(self):
        assert 3 == 3


if __name__ == "__main__":
    # pytest.main(['-vs', './test_pytest04.py'])
    pytest.main(['-vs', './test_pytest04.py', '--reruns=2', '--reruns-delay=5'])  # 多线程执行
