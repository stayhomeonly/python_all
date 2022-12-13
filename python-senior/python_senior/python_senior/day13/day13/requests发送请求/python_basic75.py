"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-11:23
   contents:
-------------------------------------------------
"""
"""
使用requests调用session鉴权的接口
"""
import requests

# 1.创建一个session对象。用来保存登录后的session鉴权信息
session = requests.Session()  # 创建对象
response = session.post(url="http://127.0.0.1:6666/business/session_login",
                        data={"username": "xiaohua", "password": "a123456", "typeId": "101"})
res = response.json()
print(res)
# 2.使用已经有访问权限的session来调用我们的session鉴权接口
response = session.post(url="http://127.0.0.1:6666/business/session_goodsInfo",
                        data={"goodsId": "", "isOnSale": "", "isPromote": ""})
res = response.json()
print(res)
