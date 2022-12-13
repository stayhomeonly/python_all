"""
-------------------------------------------------
   date      :2021/11/5-10:40
   Author    :Lee
   File Name :python_senior31
-------------------------------------------------
"""

"""
练习：不使用框架进行测试,我们也可以测试,但是比较麻烦
"""

import requests

# 1.正确流程
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={"username": "xiaoniu", "password": "123456abc"})
res = response.json()
print(res)  # {'code': '1000', 'msg': '登录成功'}

# 2.用户名错误
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={"username": "xiaoniu1", "password": "123456abc"})
res = response.json()
print(res)  # {'code': '1005', 'msg': '用户名和密码错误！'}

# 3.用户名为空
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={"username": "", "password": "123456abc"})
res = response.json()
print(res)  # {'code': '1003', 'msg': '用户名不能为空！'}

# 4.密码错误
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={"username": "xiaoniu", "password": "a1234567"})
res = response.json()
print(res)  # {'code': '1005', 'msg': '用户名和密码错误！'}

# 5.密码为空
response = requests.post(url='http://127.0.0.1:5000/user_login',
                         data={"username": "xiaoniu", "password": ""})
res = response.json()
print(res)  # {'code': '1004', 'msg': '密码不能为空！'}
