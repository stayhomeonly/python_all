"""
#@Time：2022/7/7-16:58
#@file：python_basic_24
#@Project:python_new_study
#@Content:

"""
'''1、readline读所有行数'''
def readline_count(file_name):
    return  len(open(file_name,encoding='utf-8').readlines())


if __name__ == '__main__':
    print(readline_count("stock_data.txt"))



