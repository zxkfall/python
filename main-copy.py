"""
@File: main-copy.py
@Author: Xingkun Zhang
@Email: 1475795322@qq.com
@Date: 2023/2/24 8:04
@Description: calculate column 6，7，8，9
case:
班级	id	题目1	题目2	题目3	受欢迎提名	Z班内受欢迎	保护均分	受欢迎/保护
1	1030101				0	-0.50262	1.82	1.916666667
1	2070102	4	35	5	6	0.85741	1.84	1.916666667
2	2050101	2	3	3	13	2.44411	1.85	1.916666667
2	6060102	22	3	36	3	0.1774	2.37	1.916666667
3	2070101	39	35	33	13	2.44411	2	1.916666667

"""
import pandas as pd


def generate_excel(file_path):
    data = pd.read_excel(file_path)
    current_sheet = data.values.tolist()
    end_class_num = 1
    for i in current_sheet:
        if i[0] != end_class_num:
            end_class_num = end_class_num + 1
    print(end_class_num)
    for i in range(end_class_num):
        # print('current class %s' % (i + 1))
        m = []
        for j in current_sheet:
            student_full_id = str(j[1])
            student_id = int(student_full_id[-2:])
            if j[0] == i + 1:
                if (not pd.isna(j[2])) and j[2] != student_id:
                    m.append(j[2])
                if (not pd.isna(j[3])) and j[3] != student_id:
                    m.append(j[3])
                if (not pd.isna(j[4])) and j[4] != student_id:
                    m.append(j[4])
        # print(m)
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                student_full_id = str(j[1])
                student_id = student_full_id[-2:]
                data.loc[line, '受欢迎提名'] = m.count(int(student_id))
        # print("===================")
    current_sheet = data.values.tolist()
    # print("----------------------")
    for i in range(end_class_num):
        total_people = 0
        total_sum = 0
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                total_people = total_people + 1
                total_sum = total_sum + j[5]
        average = total_sum / total_people
        # print(total_people, " ", total_sum, " ", average)
        # 离差平方和
        sum_of_squares_of_deviations = 0
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                sum_of_squares_of_deviations = sum_of_squares_of_deviations + pow(j[5] - average, 2)
        # 方差
        variance = sum_of_squares_of_deviations / total_people
        # 标准差
        standard_deviation = pow(variance, 0.5)
        total_protect_sum = 0
        total_standard = 0
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                standard = (j[5] - average) / standard_deviation
                # print('Z', standard)
                data.loc[line, 'Z班内受欢迎'] = standard
                if float(standard) > 0:
                    if float(standard) > 0:
                        total_standard = total_standard + 1
                    total_protect_sum = total_protect_sum + j[7]
                # data.loc[line, '受欢迎/保护'] = data.loc[line, '保护均分'] / standard
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                data.loc[line, '受欢迎/保护'] = total_protect_sum / total_standard
    data.to_excel(excel_writer=file_path, index=False)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print("Designed by xingkun")
    print("Version: 1.0")
    # filePath = input('Please input file Path:')
    filePath = 'bian(2).xlsx'
    generate_excel(filePath)

# 保护均分
