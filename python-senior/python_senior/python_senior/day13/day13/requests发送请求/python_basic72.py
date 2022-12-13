"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-10:21
   contents:
-------------------------------------------------
"""
import requests

"""
requests 用来模拟http请求
为什么要学习requests库：因为我们要脱离工具的测试，改用代码的形式调用接口
使用步骤：
1.pip install requests
2.导包
3.使用requests模拟请求
"""
# 发送get请求
# response = requests.get(url='http://www.baidu.com')
# print(response.text)  # 获取响应体方式1
# res_body = response.content.decode('utf-8')  # 获取响应体方式2
# print(res_body)

# 发送post请求
# response = requests.post(url='http://127.0.0.1:6666/business/token_login',
#                          data={"username": "xiaohua", "password": "a123456", "typeId": 101})
# res_body = response.content.decode('utf-8')  # 获取响应体方式2
# print(res_body)

# 对自己写的接口发请求
# get
response = requests.get(url='http://127.0.0.1:5000/login?username=xiaohua&pwd=a123456')
res_body = response.content.decode('utf-8')  # 获取响应体
print(res_body)

# post
response = requests.post(url='http://127.0.0.1:5000/login', data={"username": "xiaohua", "pwd": 'a123456'})
res_body = response.content.decode('utf-8')  # 获取响应体
print(res_body)