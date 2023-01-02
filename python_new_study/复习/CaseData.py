"""
#@Time：2022/12/28-10:43
#@file：CaseData
#@Project:git_python1
#@Content:

"""
class CaseData:
    def __init__(self, dict_case):
        for i in dict_case.items():  # 获取字典中的每一对键值对，并且进行遍历
            setattr(self, i[0], i[1])  # self.i[0]=i[1]



dict_case={"name":'冯鑫',"age":'18'}

if __name__ == '__main__':
    print(type(CaseData(dict_case)))