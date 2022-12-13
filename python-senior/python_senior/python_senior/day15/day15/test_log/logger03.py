"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/8/14-14:44
   contents:
-------------------------------------------------
"""
"""
具体的使用
"""

from logger02 import logger

try:
    num = int(input("请输入一个数字:"))
except Exception as e:
    logger.error("logger03报错！")
    logger.exception(e)
else:
    logger.info("方法正常！")
