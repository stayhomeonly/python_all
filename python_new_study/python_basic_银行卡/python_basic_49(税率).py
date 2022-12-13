"""
#@Time：2022/8/12-16:01
#@file：python_basic_49(税率)
#@Project:python_new_study
#@Content:

"""

# 需求：计算个人税后工资
gross_pay=input("请输入你的税前工资:")
# 社保基数
social_security_base=input("请输入你的社保基数：")
# 公积金的基数
reserve_base=input("请输入你的公积金基数：")
# 本年度总共工作了几个月

month_works=int(input("今年总共工作了几个月："))

if gross_pay.isdigit() and social_security_base.isdigit() and reserve_base.isdigit():
    # 去掉公积金和社保的工资
    a=float(gross_pay)-(float(social_security_base))*0.105-float(reserve_base)*0.07

    b=a-5000

    if a-5000<0:
        print("你不需要交税,你的工资:",a)
    elif  b>0 and b<=3000 :
        print("你每个月需要交的税为：",b*0.03)
        print("你的每个月工资为：", a - a * 0.03)
        print("今年税后工资为：",(a-a*0.03)*month_works)
    elif b > 3000 and b <= 12000:
        print("你每个月需要交的税为：", b * 0.1-210)
        print("你的每个月工资为：", a - (b * 0.1-210))
        print("今年税后工资为：", (a - (b * 0.1-210)) * month_works)
else:
    print("你输入税前工资、社保基数、公积金基数不是纯数字,请重新输入")


