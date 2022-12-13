"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-15:25
   contents:
-------------------------------------------------
"""
import pytest, requests

"""
1.-m 标记，我们为测试用例添加标记，并且指定运行某个标记，可以在类和方法上使用
2.需要在当前目录下，创建pytest.ini文件，并且添加标记到ini文件中
            常见的pytest.ini文件修改pytest的默认行为
            1.addopts = -vs :addopts参数可以更改默认的运行模式
            2. @pytest.mark.test01 标记case
            3.pytest.ini文件声明了测试文件匹配check_.py，测试类以Check开头，测试函数匹配check_（这个是自定义的不一定非要叫check）
            python_files = check_* *_check   # 以check_开头或者_check结尾的文件
            python_classes = Check           # 以Check开头的类
            python_functions = check_*       # 以check开头的方法
            这种就相当于重写了pytest默认的测试文件测试类和测试函数的命名规则
            这种用法一般在一些大公司会有要求命名符合自己公司的命名规范而去使用（去了公司发现定义的不是test，不要怀疑人生）
            在一般情况下，尽量不要去修改默认的命名规则
3.@pytest.mark.run(order=执行的顺序)
            使用这个run可以对我们的case的执行顺序进行排序，需要下载安装这个插件：pip install pytest-ordering
"""


class TestLogin:
    # 1、正确流程
    @pytest.mark.run(order=3)
    @pytest.mark.test01
    def test_login01(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=a123456")
        res = response.json()
        assert res == {'code': 1000, 'msg': '登录成功'}

    # 2、用户名为空
    @pytest.mark.run(order=2)
    @pytest.mark.test01
    def test_login02(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=&pwd=a123456")
        res = response.json()
        assert res == {"code": 1001, "msg": "用户名不能为空"}

    # 3、密码为空
    @pytest.mark.run(order=1)
    @pytest.mark.test02
    def test_login03(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=")
        res = response.json()
        assert res == {"code": 1002, "msg": "密码不能为空"}

    # 4、用户名错误
    @pytest.mark.test02
    def test_login04(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohu&pwd=a123456")
        res = response.json()
        assert res == {"code": 1007, 'msg': '用户名或者密码错误'}

    # 5、密码错误
    @pytest.mark.test03
    def test_login05(self):
        response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=a12345")
        res = response.json()
        assert res == {"code": 1007, 'msg': '用户名或者密码错误'}


@pytest.mark.skip(reason='下班了，没写完')
def check_register_liu(self):
    pass


if __name__ == '__main__':
    # pytest.main(['-m test01', './test_pytest_02.py'])  # 只运行test_pytest02.py模块下标记了test01的case
    # pytest.main(['-vs', '-m test03', './test_pytest_02.py'])  # 只运行test_pytest02.py模块下标记了test03的case
    pytest.main(["-vs", './test_pytest_02.py'])
