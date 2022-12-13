"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-10:24
知识点: 
---------------------------------
"""
import requests
import json

# 就是用来模拟http请求

# 1 发送get请求 直接把入参写在url里面
# res = requests.get(url='http://127.0.0.1:6666/business/token_login?username=AutoTrue&password=AutoTrue&typeId=101')
# res2 = res.json()  # .json() 是requests库自带的方法 他可以将json的响应结果转化为python里的dict
# print(res2, type(res2))

# 2 发送get请求 直接把入参写在一个dict里面 用params进行传参
dict1 = {'username': 'AutoTrue', 'password': 'AutoTrue', 'typeId': '101'}
# res3 = requests.get(url='http://127.0.0.1:6666/business/token_login', params=dict1)
# res4 = res3.json()
# print(res4)

# 发送post请求  用data进行传参的时候 默认就是 用application/x-www-form-urlencoded进行传参
# res = requests.post(url='http://127.0.0.1:6666/business/token_login', data=dict1)
# res2 = res.json()
# print(res2)

# 发送json入参的请求 把入参卸载dict里  用json进行传参  默认提交数据的的格式就是json
dict2 = {"username": "xiaozhen", "password": "a123456", "re_password": "a123456", "phone": "18822223334", "sex": "",
         "birthday": "", "qq": "","email": ""}
# res = requests.post(url='http://127.0.0.1:6666/business/regist_json', json=dict2)
# res2 = res.json()
# print(res2)

# 2 发送json入参的请求 把入参卸载dict里  用data进行传参 需要把手动把dict转化为json  需要声明入参格式的请求头 headers={'Content-Type': 'application/json'}
res = requests.post(url='http://127.0.0.1:6666/business/regist_json', data=json.dumps(dict2),
                    headers={'Content-Type': 'application/json'})
res2 = res.json()
print(res2)
