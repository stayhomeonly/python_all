"""
#@Time：2022/6/18-16:24
#@file：python_basic_01
#@Project:python_new_study
#@Content:

"""
import json

# json格式，json格式本质上就是字符串类型的字典
"""例如单个学员信息"""
stu1 = '{"name":"张三","age":"18","hoddy":"play"}'
# json 格式括号里面必须是双引号，外面为单引号
"""例如多个学员学院信息"""
stus = '[{"name":"张三","age":"18","hoddy":"play"},' \
       '{"name": "李四", "age": "18", "hoddy": "play"}]'

# 1.json 转换为python(转换成字典，列表嵌套字典)
jsonData = '{"name":"张三","age":"18","hoddy":"play"}'
PythonData = json.loads(jsonData)
print(PythonData, type(PythonData))

# 2.python转换为json()，
pythonData = {"cname": "1001", "cpwd": "123", "cbalance": "1000", "name": "张三"}
r = str(pythonData)  # XXXXXX错误的转换
print(r)
# 2.1 python转换为json()，如果里面有中文，ensure_ascii=False
jsonData = json.dumps(pythonData, ensure_ascii=False)  # ensure_ascii=False 禁止ascii转换
print(jsonData, type(jsonData))
