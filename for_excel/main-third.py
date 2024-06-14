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
        # calculate result
        calculate_result(current_sheet, data, end_class_num)
        # rewrite result
        data.to_excel(excel_writer=file_path, index=False)




def calculate_result(current_sheet, data, end_class_num):
    for i in range(end_class_num):
        total_people = 0
        total_sum = 0
        for j in current_sheet:
            print(j, i)
            if j[0] == i + 1:
                total_people = total_people + 1
                if pd.isna(j[2]):
                    total_sum = total_sum + 0
                else:
                    total_sum = total_sum + j[2]
        if total_people == 0:
            break
        average = total_sum / total_people
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                data.loc[line, '班级反欺凌'] = average


def get_total_class(current_sheet):
    end_class_num = 1
    for i in current_sheet:
        if i[0] != end_class_num:
            end_class_num = end_class_num + 1
    return end_class_num


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print("Designed by xingkun")
    print("Version: 1.0")
    print("Note:")
    print("1.for case 3")
    filePath = input('Please input file Path:')
    # filePath = 'popular2.xlsx'
    generate_excel(filePath)