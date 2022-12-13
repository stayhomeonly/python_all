"""
#@Time：2022/11/26-20:52
#@file：python_basic_67(电子钱包)
#@Project:git_python
#@Content:

"""


# 电子钱包功能

def login():
    print('执行登录功能')


def scan():
    print('执行扫码支付功能')


def translate():
    print('执行转账功能')


def query():
    print('执行查询余额功能')


def recharge():
    print('执行充值功能')


# while
# True:
# print('''
#     0 退出
#     1 登录
#     2 扫码支付
#     3 转账
#     4 查询余额功能
#
#     5 充值功能
#
#     ''')
# opt = input('请输入功能编号>>>')
# if opt == '0':
#     break
# elif opt == '1':
#     login()
# elif opt == '2':
#     scan()
#
# elif opt == '3':
#     scan()
# elif opt == '4':
#     query()
# elif opt == '5':
#     recharge()
# else:
#     print('没有此功能，傻子')


# 需求：如果以后需要加功能每次都是加elif 代码质量非常差，所以来优化
# 优化方案
# fund_dict = {
#     '1': login, '2': scan, '3': translate, '4': recharge
# }
#
# while True:
#     print('''
#     0 退出
#     1 登录
#     2 扫码支付
#     3 转账
#     4 查询余额功能
#
#     5 充值功能
#
#     ''')
#     opt = input('请输入功能编号>>>')
#     if opt == '0':
#         break
#     # if opt in fund_dict:
#     #     fund_dict[opt]()
#     # else:
#     #     print('此功能不存在')
#
#     # 上面if的写法其实没有问题，但是如果我的代码越写越多，缩进就越多，修改就很烦
#     # 所以修改优化
#     if opt not in fund_dict:
#         print('此功能不存在')
#         continue
#     fund_dict[opt]()

# 如何把代码做一个优化，不用本次增加一个，就去添加一个
fund_dict = {
    '0': [None, '退出'],
    '1': [login, '登录'],
    '2': [scan, '扫码支付'],
    '3': [translate, '执行转账'],
    '4': [recharge, '执行充值功能']
}

while True:
    for key in fund_dict:
        print(key, fund_dict[key][1])
    opt = input('请输入功能编号>>>')
    if opt == '0':
        break
    # if opt in fund_dict:
    #     fund_dict[opt]()
    # else:
    #     print('此功能不存在')

    # 上面if的写法其实没有问题，但是如果我的代码越写越多，缩进就越多，修改就很烦
    # 所以修改优化
    if opt not in fund_dict:
        print('此功能不存在')
        continue
    fund_dict[opt][0]()
