"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/8/14-14:39
   contents:
-------------------------------------------------
"""
"""
封装日志模块
"""

import logging


def get_logger():
    # 第二步：创建日志对象
    logger = logging.getLogger()
    logger.setLevel('DEBUG')  # 代表获取DEBUG及DEBUG级别以上的内容
    # logger.setLevel(10)  # 代表获取DEBUG及DEBUG级别以上的内容

    # 第三步：设置输出方向
    sh1 = logging.StreamHandler()
    sh1.setLevel("INFO")  # 代表获取INFO及INFO级别以上的内容

    # 输出info级别的日志，并且内容为追加写入(mode='a')
    sh2 = logging.FileHandler(filename='./info.log', mode='a', encoding='utf-8')
    sh2.setLevel(20)

    # # 输出error级别的日志，并且内容为追加写入(mode='a')
    # sh3 = logging.FileHandler(filename='./info.log', mode='a', encoding='utf-8')
    # sh3.setLevel(40)

    # 第四步：添加输出方向到logger对象
    logger.addHandler(sh1)
    logger.addHandler(sh2)
    # logger.addHandler(sh3)

    # 第五步：设置输出格式
    log_format = '%(asctime)s----%(levelname)s--%(lineno)d-:%(message)s'
    my_fmt = logging.Formatter(log_format)
    sh1.setFormatter(my_fmt)
    sh2.setFormatter(my_fmt)
    # sh3.setFormatter(my_fmt)
    return logger


logger = get_logger()
