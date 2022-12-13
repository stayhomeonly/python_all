"""
---------------------------------
作者: Mr.Liu
创建时间: 2022/8/7-14:33
知识点: 
---------------------------------
"""


# 复习
# 设计一个类，可以将字典转为对象
# 字典API：
#       items() 获取所有的键值对
#       keys()  获取所有的键
#       Values() 获取所有的值
class CaseData:
    # def case_data(self, dict_case):
    #     for i in dict_case.items():
    #         setattr(self,i[0],i[1])
    def __init__(self, dict_case):
        for i in dict_case.items():
            setattr(self, i[0], i[1])


case = {'username': 'xiaoliu', 'pwd': 'a123456', 're_pwd': 'a123456'}

case1 = CaseData(case)
print(case1.username)
print(case1.pwd)
print(case1.re_pwd)

# 将存放多个字典的列表转换为对象，并且存放在一个空列表当中
cases = [{'username': 'xiaoliu1', 'pwd': 'a123456', 're_pwd': 'a123456'},
         {'username': 'xiaoliu2', 'pwd': 'a123456', 're_pwd': 'a123456'},
         {'username': 'xiaoliu3', 'pwd': 'a123456', 're_pwd': 'a123456'},
         {'username': 'xiaoliu4', 'pwd': 'a123456', 're_pwd': 'a123456'},
         {'username': 'xiaoliu5', 'pwd': 'a123456', 're_pwd': 'a123456'}]

datas = []
for i in cases:
    case = CaseData(i)
    datas.append(case)

print(datas[4].username)