"""
#@Time：2022/6/21-21:48
#@file：python_basic_08
#@Project:python_new_study
#@Content:

"""
# a 追加写入模式,不能读取
f=open("name_list",mode="a")
f.write('heheh')
f.write('jack')
f.close()
