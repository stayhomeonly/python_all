stu_list = [['李渊', 82], ['李世⺠', 7], ['侯君集', 5], ['李靖', 58], ['魏征',
                                                             41], ['房⽞龄', 64], ['杜如晦', 65], ['柴绍', 94], ['程知节', 45],
            ['尉迟恭', 94],
            ['秦琼', 54], ['⻓孙⽆忌', 85], ['李存恭', 98], ['封德彝', 16], ['段志⽞', 44], ]
new_stu_list = [
    [],
    [],
    [],
    [],
    []
]
for i in stu_list:
    print(i[1])

    if i[1] >= 90 and i[1] <= 100:
        new_stu_list[0].append(i)


    elif i[1] >= 80 and i[1] <= 89:
        new_stu_list[1].append(i)

    elif i[1] >= 70 and i[1] <= 79:
        new_stu_list[2].append(i)

    elif i[1] >= 60 and i[1] <= 69:
        new_stu_list[3].append(i)

    else:

        new_stu_list[4].append(i)

print(new_stu_list)
