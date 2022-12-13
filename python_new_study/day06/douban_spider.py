# coding:utf-8
"""
#@Time：2022/11/20-20:42
#@file：douban_spider
#@Project:python_new_study
#@Content:

"""
import requests  # 下载网页
import bs4  # beautifulSoup ,解析网页

page_obj=requests.get("https://www.douban.com/note/820479376/?_i=8948366uPKuDCW")
print(page_obj.text)
