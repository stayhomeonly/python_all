"""
#@Time：2022/6/21-21:15
#@file：python_basic_06
#@Project:python_new_study
#@Content:

"""
# w是创建模式，会覆盖之前所有的内容，但是不支持读,追加写入每次写入一个参数
f = open("name_list", mode="w")
f.write("张三\n") #\n换行符
f.write("李四\n")
f.write("金大王\n")
f.write("Alex\n")
f.close()

