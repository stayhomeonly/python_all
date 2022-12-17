"""
#@Time：2022/12/11-20:20
#@file：python_basic_75(yield)
#@Project:git_python
#@Content:

"""


# yield表达式
def func(x):
    print(f'{x}开始执行')
    while True:
        y = yield None  # yield，就是暂停在那里，然后返回一个值，如果yield后面不写，就是返回None
        print('\n', x, y, '\n')


g = func(1)
# g.send(None) # next(g)
# g.send(None)
next(g)
g.send(10) # send是在给yield传值


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


f = foo()
print(next(f))
print("*" * 20)
print(f.send(7))  # 这里调用send()函数给生成器给res赋值7，然后继续调用next(f)，返回4

# 结果
'''
starting...
4
********************
res: 7
4
'''
