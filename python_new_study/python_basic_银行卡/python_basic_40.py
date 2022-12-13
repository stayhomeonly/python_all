"""
#@Time：2022/7/30-20:02
#@file：python_basic_40
#@Project:python_new_study
#@Content:

"""


# 1. 要求⽤户输⼊姓名、年龄、⼿机号、身份证号、所选课程，然后为学员完成注册
# 2. ⼿机号、身份证号唯⼀
# 3. 可选的课程只能从Python、Linux、⽹络安全、前端、数据分析 这⼏⻔⾥选
# 4. 学员信息存⼊⽂件

db_file="student_data.db"


def register():
    stu_data={}
    name = input("请输入你的姓名:").strip()  # 如果不加上strip()就不去掉换行符
    age = input("请输入你的年龄:").strip()
    phone_num = input("请输入你的手机号码:").strip()
    id = input("请输入你的身份证号码:").strip()
    course_list = ["Python", "Linux", "⽹络安全", "前端", "数据分析"]
    for index,course in enumerate(course_list):
        print(f'{index},{course}')
    selected_course=input("选择想要学的课：")
    if selected_course.isdigit():
        selected_course=int(selected_course)
        if selected_course>=0 and selected_course<len(course_list):
            pick_course=course_list[selected_course] #选中的课
        else:
            exit("输入课程不正确")
    else:
        exit("非法输入")

    stu_data['name']=name
    stu_data['age'] = age
    stu_data['phone_num'] = age
    stu_data['id'] = id
    stu_data['course'] = pick_course

    return stu_data

def commit_to_db(filename,stu_data):
    """

    :param filename: 打开文件名称
    :param stu_data: 学员的数据库
    :return:
    """
    f=open(filename, "a")
    row=f'{stu_data["name"]},{stu_data["age"]},{stu_data["phone_num"]},{stu_data["id"]},{stu_data["course"]}\n'
    f.write(row)
    f.close()

student_data=register()
print(student_data)
commit_to_db(db_file,student_data)


