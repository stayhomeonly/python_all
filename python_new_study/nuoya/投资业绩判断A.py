"""
#@Time：2022/8/17-14:45
#@file：投资业绩判断
#@Project:python_new_study
#@Content:

"""


# 判断级别是否为A
class Gudge_Level_A():
    list1 = ["退出期", "延长期", "清算期"]
    fund_term = input("请输入子基金的基金期限:")
    if fund_term not in list1:
        print("子基金的投资业绩级别为A")
        exit()

    while True:
        try:
            DPI = input("请输入DPI:")  #
            if isinstance(eval(DPI), float):
                if float(DPI) >= 2:
                    print("子基金的投资业绩级别为A")
                    exit()
                else:
                    print("请调用其他函数判断子基金投资业绩的级别,肯定不是A")
                    break
        except  Exception as e:
            print("你输入的不是浮点数数字")
            # raise e
        else:
            print("请重新输入DPI:")


class Gudge_Level_C():
    try:
        TVPI = input("请输入最近一期TVPI的值:")
        if isinstance(eval(TVPI), float):
            if float(TVPI) < 1:
                print("子基金的投资业绩的级别为C")
                exit()
        # 如果没有往期的数据，该判断应该注释掉
        TVPI_last = input("请输入最近一期同期TVPI的值:")
        if isinstance(eval(TVPI_last), float):
            if (float(TVPI) - float(TVPI_last)) / float(TVPI_last) < -0.5:
                print("子基金的投资业绩的级别为C")
                exit()
        # 同期子基金的中位数
        same_perio_fund = input("请输入同期子基金TVPI的中位数:")
        # 同期子基金DPI排名
        same_perio_fund_DPI = input("请输入同期子基金的DPI排名百分比:")  # 直接输入小数

        if isinstance((eval(same_perio_fund), eval(same_perio_fund)), float):
            if float(TVPI) < ((float(same_perio_fund) - 1) * 0.5 + 1) and float(same_perio_fund_DPI) > 0.75:
                print("子基金的投资业绩的级别为C")
                exit()
    except Exception as e:
        print("请检查TVPI、TVPI_last、same_perio_fund、same_perio_fund_DPI是否输入的是纯数字")
        raise e

    else:
        print('子基金的投资业绩的级别肯定不为C')


class Gudge_Level_B():
    try:
        TVPI = input("请输入最近一期TVPI的值:")
        # 同期子基金TVPI的中位数
        same_perio_fund = input("请输入同期子基金TVPI的中位数:")
        if isinstance((eval(TVPI), eval(same_perio_fund)), float):
            if float(TVPI) < (float(same_perio_fund) - 1) * 0.5 + 1:
                print("子基金的投资业绩的级别为B")
                exit()
        # 同期子基金DPI排名
        same_perio_fund_DPI = input("请输入同期子基金的DPI排名百分比:")  # 直接输入小数
        if isinstance(eval(same_perio_fund_DPI), float):
            if float(same_perio_fund_DPI) > 0.75:
                print("子基金的投资业绩的级别为B")
                exit()
    except Exception as e:
        print("你输入的不是浮点型")
        raise e
    else:
        print('子基金的投资业绩的级别肯定不为B')


if __name__ == '__main__':
    Gudge_Level_A()
