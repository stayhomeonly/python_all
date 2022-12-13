"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-14:12
   contents:
-------------------------------------------------
"""
import pytest
import requests

"""
1、pytest的作用：  用来管理和运行测试用例
2、pytest安装：pip install pytest
3、查看是否安装成功：pytest --version
4、测试用例编写规则：
    1.模块名必须以test_开头 或者 _test结尾
    2.测试类必须以Test开头，并且不能有__init__方法
    3.测试方法必须以test开头
5、常用的断言（比较预期结果和实际结果是否一致，并且返回比较结果）
    assert A==B
    assert A>B
    assert A in B
"""
age = 17


class TestLogin:
    # 1、正确流程
    # skipif 条件触发后会跳过测试用例
    @pytest.mark.skipif(age < 18, reason="年龄低于18岁不测试这个case")
    def test_login01(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=a123456")
        res = response.json()
        assert res == {'code': 1000, 'msg': '登录成功'}

    # 2、用户名为空
    def test_login02(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=&pwd=a123456")
        res = response.json()
        assert res == {"code": 1001, "msg": "用户名不能为空"}

    # 3、密码为空
    def test_login03(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=")
        res = response.json()
        assert res == {"code": 1002, "msg": "密码不能为空"}

    # 4、用户名错误
    def test_login04(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohu&pwd=a123456")
        res = response.json()
        assert res == {"code": 1007, 'msg': '用户名或者密码错误'}

    # 5、密码错误
    def test_login05(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=a12345")
        res = response.json()
        assert res == {"code": 1007, 'msg': '用户名或者密码错误'}


class TestRegister:
    def test_register(self):
        print("这个是注册")


@pytest.mark.skip(reason='下班了，没写完')
def test_register_liu(self):
    pass


if __name__ == '__main__':
    # 知识点1：运行该模块下所有的测试用例
    pytest.main(["./test_pytest_01.py"])  # 运行指定模块
    # 知识点2：-s -v -q 命令参数
    # pytest.main(['-v', './test_pytest_01.py'])  # 运行指定模块，-v是详细信息模式，输出更详细的执行用例信息
    # pytest.main(['-q', './test_pytest_01.py'])  # 运行指定模块，-q是静默模式，只显示运行结果
    # pytest.main(['-s', './test_pytest_01.py'])  # 运行指定模块，-s是显示用例中的打印信息和日志信息
    # 知识点3：运行模块中的某个类
    # pytest.main(["./test_pytest_01.py::TestLogin"])  # 运行指定模块下的某个类
    # pytest.main(["-vs", "./test_pytest_01.py::TestRegister"])  # 运行指定模块下的某个类，-vs详细显示用例并展示打印信息和日志信息
    # 知识点4：运行模块中的某个用例
    # pytest.main(["-vs", './test_pytest_01.py::TestLogin::test_login02'])  # 运行指定用例
    # pytest.main(["-vs", './test_pytest_01.py::test_register_liu'])  # 运行指定用例(只能找到写在最外面的函数，写在类当中的需要先找到对应的类)
    # 知识点5：运行某个目录下的所有用例
    # 相对路径和绝对路径
    # 相对路径的./代表同一级目录   ../代表上一级目录
    # pytest.main(['./'])  # 相对路径的写法
    # pytest.main([r'C:\Users\xg\Desktop\Python_gaoji\day13\test_pytest测试用例编写和执行']) 绝对路径的写法
    # 知识点6：只运行包含指定关键字的用例，比如：匹配当前目录下包含liu的测试用例（不区分大小写，匹配目录名、模块名、类名、用例名）
    # pytest.main(["-vs", '-k liu'])  # 运行当前目录下包含liu的用例
    # pytest.main(["-vs", '-k liu', './test_pytest_01.py'])  # 运行指定模块下包含liu的用例
