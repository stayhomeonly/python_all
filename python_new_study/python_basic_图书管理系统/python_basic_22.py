"""
#@Time：2022/7/2-22:37
#@file：python_basic_22
#@Project:python_new_study
#@Content:

"""
accounts = {
    # "alex":["alex","abc123","1"
}

f = open('account.db', 'r')
for line in f:
    line = line.strip().split(
        ',')  # 加上strip(){'alex': ['alex', 'adc123', '1'], 'jack': ['jack', 'adc123', '0'], 'rain': ['rain', 'adc123', '0']}
    accounts[line[0]] = line
print(accounts)
# 如果不加上strip()就不去掉换行符
# {'alex': ['alex', 'adc123', '1\n'],
# 'jack': ['jack', 'adc123', '0\n'],
# 'rain': ['rain', 'adc123', '0']}

# 需求：设计一个登录界面，密码只输入三次就锁定


while True:
    username = input('请输入用户名：').strip()
    if username in accounts:
        count = 0
        while count < 3:
            passwd = input("请输入密码:")

            if passwd == accounts[username][1]:
                print("恭喜你登录成功")
                exit()
            else:
                count = count + 1
                if count < 3:
                    print("密码输入错误")
                else:
                    print("密码输入错误次数超过当日限制次数")


        if count ==3:
            print(f"输错了{count}次密码,需要锁定账号{username}")
            # 先改内存中dict账号信息的用户状态
            # 把dict里的数据转成account.db数据格式，并且存回文件


    else:
        print("该用户名未注册,请输入已经注册的用户名")
        continue
