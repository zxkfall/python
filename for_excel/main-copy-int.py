"""
@File: main-copy.py
@Author: Xingkun Zhang
@Email: 1475795322@qq.com
@Date: 2023/2/24 8:04
@Description:
"""
import pandas as pd


def generate_excel(file_path):
        data = pd.read_excel(file_path)
        current_sheet = data.values.tolist()
        # get all class
        end_class_num = get_total_class(current_sheet)
        print(end_class_num)
        # count popular student num
        count_popular_student_num(current_sheet, data, end_class_num)
        current_sheet = data.values.tolist()
        # calculate result
        calculate_result(current_sheet, data, end_class_num)
        # rewrite result
        data.to_excel(excel_writer=file_path, index=False)



def calculate_result(current_sheet, data, end_class_num):
    for i in range(int(current_sheet[0][0]) - 1,end_class_num):
        total_people = 0
        total_sum = 0
        for j in current_sheet:
            if j[0] == i + 1:
                total_people = total_people + 1
                if pd.isna(j[5]):
                    total_sum = total_sum + 0
                else:
                    total_sum = total_sum + j[5]
        if total_sum == 0:
            break
        average = total_sum / total_people
        # 离差平方和
        sum_of_squares_of_deviations = 0
        for j in current_sheet:
            if j[0] == i + 1:
                sum_of_squares_of_deviations = sum_of_squares_of_deviations + pow(j[5] - average, 2)
        # 方差
        variance = sum_of_squares_of_deviations / total_people
        # 标准差
        standard_deviation = pow(variance, 0.5)
        if standard_deviation == 0:
            print('standard deviation can not be zero, current class is ' + str(i + 1))
            break
        total_protect_sum = 0
        total_standard = 0
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                standard = (j[5] - average) / standard_deviation
                data.loc[line, 'Z班内受欢迎'] = standard
                if float(standard) > 0:
                    if float(standard) > 0:
                        total_standard = total_standard + 1
                    total_protect_sum = total_protect_sum + j[7]
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                data.loc[line, '受欢迎/保护'] = total_protect_sum / total_standard


def count_popular_student_num(current_sheet, data, end_class_num):
    for i in range(int(current_sheet[0][0]) - 1,end_class_num):
        m = []
        for j in current_sheet:
            student_id = get_student_id(j)
            print(j)
            if j[0] == i + 1:
                add_student_id(j[2], m, student_id)
                add_student_id(j[3], m, student_id)
                add_student_id(j[4], m, student_id)
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                data.loc[line, '受欢迎提名'] = m.count(get_student_id(j))


def get_total_class(current_sheet):
    end_class_num = 1
    for i in current_sheet:
        if i[0] != end_class_num:
            end_class_num = end_class_num + 1
    return end_class_num


def get_student_id(current_line):
    student_full_id = str(int(current_line[1]))
    student_id = int(str(student_full_id[-2:]))
    return student_id


def add_student_id(current_id, result, student_id):
    if not str(current_id).isspace() and pd.notna(current_id) and int(current_id) != student_id:
        result.append(int(current_id))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print("Designed by xingkun")
    print("Version: 1.1")
    print("Note:")
    print("1. can trim space, Optimize algorithm logic")
    print("2. add error tips")
    filePath = input('Please input file Path:')
    # filePath = 'popular2.xlsx'
    generate_excel(filePath)

# 保护均分
