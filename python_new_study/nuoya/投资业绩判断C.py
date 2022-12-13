"""
#@Time：2022/8/17-14:45
#@file：投资业绩判断
#@Project:python_new_study
#@Content:

"""


# 判断级别为C
class Gudge_level_C():
    TVPI=input("请输入最近一期TVPI的值:")
    if TVPI.isdigit():
        if float(TVPI)<1:
            print("子基金的投资业绩的级别为C")
            exit()
    TVPI_last=input("请输入最近一期同期TVPI的值:")
    if TVPI_last.isdigit():
        if (float(TVPI)-float(TVPI_last)/float(TVPI_last))<-0.5:
            print("子基金的投资业绩的级别为C")
            exit()
    #同期子基金的中位数
    same_perio_fund=input("请输入同期子基金的中位数:")
    # 同期子基金DPI排名
    same_perio_fund_DPI=input("请输入同期子基金的DPI排名百分比:")
    if same_perio_fund.isdigit():
        if float(TVPI)<(float(same_perio_fund)-1)*0.5+1 and float(same_perio_fund_DPI)>0.75:
            print("子基金的投资业绩的级别为C")
            exit()
    else:
        print("请检查TVPI、TVPI_last、same_perio_fund、same_perio_fund_DPI是否输入的是纯数字")


if __name__ == '__main__':
    Gudge_level_C()
