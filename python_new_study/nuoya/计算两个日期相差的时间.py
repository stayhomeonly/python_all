"""
#@Time：2022/8/17-16:55
#@file：123
#@Project:python_new_study
#@Content:

"""

import time

st = "2021-03-05 00:00:00"
et = "2021-03-09 23:59:59"


def tm_array(day1, day2):
    time_array1 = time.strptime(''.join(day1.split(' ')[0]), "%Y-%m-%d")
    timestamp_day1 = int(time.mktime(time_array1))
    time_array2 = time.strptime(''.join(day2.split(' ')[0]), "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result


# 判断投资进度的级别
class Investment_Progress():
    # 最新报告截止日所处期限
    deadline_of_latest_report = input("请输入所处于的期限:")
    res = deadline_of_latest_report.strip()  # 去掉输入的时候的空格
    if res != "投资期":
        print("投资基金进度为A")
        exit()

    # 投资进度
    investment_progress = input("请输入投资进度:")
    # 最新报告截止日期
    report_due_date = input("请输入报告截止日期")
    # 基金成立日
    fund_establishment_date = input("请输入基金成立日")
    # 投资期限
    term_of_investment = input("请输入投资期限")
    if isinstance(eval(investment_progress), float) and term_of_investment.isdigit():
        if float(eval(investment_progress)) < (tm_array(report_due_date, fund_establishment_date) /
                                               (int(term_of_investment) * 365)) * 0.5:
            print("投资基金进度为C")
            exit()
