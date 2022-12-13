"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-11:16
   contents:
-------------------------------------------------
"""
import requests

"""
requests 模拟接口之间的关联

什么是接口关联？ 一个接口的入参是另一个接口的出参
"""
# 1.先进行登录
response = requests.post(url='http://127.0.0.1:6666/business/token_login',
                         data={"username": "xiaohua", "password": "a123456", "typeId": "101"})
res = response.json()  # 将响应结果转换为字典
print(res, type(res))
tk = res["token"]
print(tk)

response = requests.get(
    url="http://127.0.0.1:6666/business/token_goodsInfo?token={}&goodsId=&isOnSale=&isPromote=".format(tk))
res = response.json()  # 将响应结果转换为字典
print(res)