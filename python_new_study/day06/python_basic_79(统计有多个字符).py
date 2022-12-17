"""
#@Time：2022/12/17-20:57
#@file：python_basic_79(统计有多个字符)
#@Project:git_python1
#@Content:

"""
# 统计有多个字符
with open('./use.log', mode='rt', encoding='utf-8') as f:
    # 第一种方法：读取文件内所有的内容，但是有一个弊端，就是如果文件内容过多，会导致内存爆了，所以
    # 不见建议这样使用
    # res=f.read()
    # print(len(res))

    # size=0
    # # 第二种办法,但是方案不够简洁
    # for line in f:
    #     res=len(line)
    #     size =size+res
    # print(size)

    # 第三种方法,更加简单，但是如果行数过多，还是占用内存
    # res = sum([len(line) for line in f])
    # print(res)

    # 第四种办法，相比较第三种办法,列表生成式改为迭代器
    res = sum((len(line) for line in f))
    print(res)
