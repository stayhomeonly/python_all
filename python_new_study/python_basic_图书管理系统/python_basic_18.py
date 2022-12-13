"""
#@Time：2022/6/29-14:23
#@file：python_basic_18
#@Project:python_new_study
#@Content:

"""
l = [1, 7, 2, 3, 8, 2, 4, 6,98]
print(l.index(8))
# 用二分法算法找出8
def search(l,m):
    """

    :param l: l是列表
    :param m: 需要取到的值
    :return: 如果列表l为空，结束递归
    """
    # 先给列表按照升序排列
    l.sort()
    print(l)
    #开始下标
    index_star=0
    #结束下标
    end_index=len(l)-1
    #中间下标
    middle_index=len(l)//2
    if len(l) == 0:  # 当最后切出来的列表为空的时候，就说明值不存在
        print('该值不存在')
        return

    elif l[middle_index]>m:
        l=l[index_star:middle_index]
        search(l,m)
    elif l[middle_index]<m:
        l=l[middle_index+1:end_index+1]
        search(l, m)
    else:
        print('找到了')

search(l, 98)



