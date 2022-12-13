"""
#@Time：2022/7/22-22:24
#@file：python_basic_29
#@Project:python_new_study
#@Content:

"""
class Card():
    def __init__(self,cnum,cpwd,cname,cbalance):
        self.bankName="python银行"
        self.cnum= cnum
        self.cpwd = cpwd
        self.cname = cname
        self.__cbalance = cbalance   # 属性一旦加上__就会变成私有属性，就只能在类的内部使用

    def showBalance(self):
        r=self.__login()
        if r=="OK":

            print(f"余额:{self.__cbalance}元")

    def __login(self): # 加上__变成了私有方法
        num=input("请输入卡号：")
        pwd = input("请输入密码：")
        if  num==self.cnum and pwd ==self.cpwd:
            print("验证成功")
            return "OK"
        else:
            print("验证失败")
            return "no"


    def deposit(self):
        r=self.__login() #可以在类的内部调用其他方法
        if r=="OK":
            money=float(input("请输入存款金额:"))
            self.__cbalance += money
            print(f"存款成功！存入{money}元,余额{self.__cbalance}元")

if __name__ == '__main__':
    c1=Card("1001","123","张三",1000)

    c1.deposit()



