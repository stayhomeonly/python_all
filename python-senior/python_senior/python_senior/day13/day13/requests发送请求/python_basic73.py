"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/7/24-10:50
   contents:
-------------------------------------------------
"""
import requests, json

"""
requests模拟json请求（请求体数据为json格式）
"""
"""
# dumps、loads、dump、load的区别
# json.load：表示读取文件，返回python对象
# json.dump:表示写入文件，文件为json字符串格式，无返回
# json.dumps:将python中的字典类型转换为字符串类型(text)，返回json字符串
注意：使用json.dumps时，必须添加请求体信息，设置为json格式
# json.loads:将json字符串转换为字典类型，返回python对象
"""

# 写法一
# post
response = requests.post(url='http://127.0.0.1:6666/business/regist_json', json={"username": "xiaohua1",
                                                                                 "password": 'a123456',
                                                                                 "re_password": 'a123456',
                                                                                 "phone": '13487280000', "sex": '',
                                                                                 "birthday": '',
                                                                                 "qq": '', "email": ''})
res_body = response.content.decode('utf-8')  # 获取响应体
print(res_body)

# 写法二
response = requests.post(url='http://127.0.0.1:6666/business/regist_json',
                         data=json.dumps({"username": "xiaohua1",
                                          "password": 'a123456',
                                          "re_password": 'a123456',
                                          "phone": '13487280000',
                                          "sex": '',
                                          "birthday": '',
                                          "qq": '', "email": ''})
                         , headers={"Content-Type": "application/json"})
res_body = response.content.decode('utf-8')  # 获取响应体
print(res_body)
