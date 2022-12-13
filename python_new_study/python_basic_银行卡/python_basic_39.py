"""
#@Time：2022/7/30-19:32
#@file：python_basic_39
#@Project:python_new_study
#@Content:

"""
course_list = ['python开发', 'Linux云计算']
for index, course in enumerate(course_list):
    print(f'{index}.{course}')  # 遍历出索引，以及索引对应的数据

# 如果不想索引从0 开始，可以更改
a=list(enumerate(course_list,start=1))
print(a)
