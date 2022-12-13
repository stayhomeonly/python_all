"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-11:33
   contents:
-------------------------------------------------
"""
import requests

"""
请简单的测试一下我们自己写的登录接口
不使用框架进行测试，我们也可以测试，但是比较麻烦
"""
# 1、正确流程
response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=a123456")
res = response.json()
if res == {'code': 1000, 'msg': '登录成功'}:
    print("True")
else:
    print("False")

# 2、用户名为空的场景
response = requests.get(url="http://127.0.0.1:5000/login?username=&pwd=a123456")
res = response.json()
if res == {"code": 1001, "msg": "用户名不能为空"}:
    print("True")
else:
    print("False")

# 3、密码为空
response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=")
res = response.json()
if res == {"code": 1002, "msg": "密码不能为空"}:
    print("True")
else:
    print("False")

# 4、用户名错误
response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohu&pwd=a123456")
res = response.json()
if res == {"code": 1007, 'msg': '用户名或者密码错误'}:
    print("True")
else:
    print("False")

# 5、密码错误
response = requests.get(url="http://127.0.0.1:5000/login?username=xiaohua&pwd=a12345")
res = response.json()
if res == {"code": 1007, 'msg': '用户名或者密码错误'}:
    print("True")
else:
    print("False")
