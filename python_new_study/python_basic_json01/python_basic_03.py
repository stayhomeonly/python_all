"""
#@Time：2022/6/19-20:55
#@file：python_basic_03
#@Project:python_new_study
#@Content:

"""
import json

# 写入初始数据 记得要使用程序编写，否则可能会报编码错误
import datetime
import time

d = '[{"时间": "2021/03/04 15:20:21", "项目": "收到王敏货款", "金额": 20000, "分类": "收入"}, {"时间": "2021/04/18 19:59:41", "项目": "吃饭", "金额": 23.0, "分类": "支出"}, {"时间": "2021/04/18 20:00:12", "项目": "买手机", "金额": 4000.0, "分类": "支出"}, {"时间": "2021/04/18 21:03:32", "项目": "吃饭", "金额": 5.0, "分类": "支出"}, {"时间": "2021/04/18 21:06:07", "项目": "买菜", "金额": 34.0, "分类": "支出"}, {"时间": "2021/04/18 21:06:28", "项目": "发工资", "金额": 23000.0, "分类": "收入"}]'
with open(r"data.txt", "w") as f:
    f.write(d)


# 初始数据一定要通过程序写入
# 一个文本文件中只能保存一种业务对象

# 读json数据
def readData():
    with open(r"data.txt", "r") as f:
        jsonData = f.read()
    datalist = json.loads(jsonData)
    return datalist


# 写json数据
def writeData(dataList):
    jsonData = json.dumps(dataList, ensure_ascii=False)
    with open(r"data.txt", "w") as f:
        f.write(jsonData)
        print("数据写入成功")


# 显示账目
def showData():
    sumIn=0 #总收入
    sumOut = 0  # 总开支


    dataList = readData()
    print("******************账单****************")
    for data in dataList:

        if data['分类']=='支出':
            sumOut=sumOut+int(data['金额'])
            print(data['时间'], "  ", data['项目'], "  ", data['金额']*-1)
        else:
            sumIn=sumIn + int((data['金额']))
            print(data['时间'], "  ", data['项目'], "  ", data['金额'])
    print("***************************************")
    print("****总收入：",sumIn,"元,总开支：",sumOut,"元，结余:",sumIn-sumOut,"元！")


# 增加一笔账目
def addData():
    dataList=readData()
    content=input("请输入账单明细:")
    amount = float(input("请输入账单金额:"))
    c=int(input("请选择(1.收入 2.支出):"))
    cla="支出"
    if c==1:
        cla="收入"
    t=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    newData={"时间": t, "项目": content, "金额": amount, "分类": cla}
    dataList.append(newData)
    writeData(dataList)


if __name__ == '__main__':
    showData()
    addData()
    showData()
