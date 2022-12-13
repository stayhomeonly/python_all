"""
#@Time：2022/8/11-21:04
#@file：python_basic_47(json)
#@Project:python_new_study
#@Content:

"""
import requests,json
url="www.baidu.com"
data={"name":"冯鑫","age":"30"}
# 需要传送json
requests.post(url=url,data=json.dumps(data))
# 另外一种写法
requests.post(url=url,json=data)