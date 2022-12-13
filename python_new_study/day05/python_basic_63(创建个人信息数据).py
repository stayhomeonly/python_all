# coding:utf-8
"""
#@Time：2022/11/7-16:47
#@file：python_basic_63
#@Project:python_new_study
#@Content:

"""
import os
from faker import Faker
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用

wb = workbook.Workbook()  # 创建Excel对象
faker = Faker("zh-CN")
ws = wb.active  # 获取当前正在操作的表对象
# 往表中写入标题行,以列表形式写入！
ws.append(['序号', '姓名', '身份证号码', '手机号', '公司邮箱', '公司名', '邮编', '家庭住址'])
# 随机生成15条数据存入Excel中

for i in range(15):
    ws.append(
        [i, faker.name(), faker.ssn(), faker.phone_number(), faker.company_email(), faker.company(), faker.postcode(),
         faker.address()])
wb.save('faker.xlsx')
