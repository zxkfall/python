"""
@File: main-second.py
@Author: Xingkun Zhang
@Email: 1475795322@qq.com
@Date: 2023/2/24 19:11
@Description: 
"""
import pandas as pd

if __name__ == '__main__':
    print("Designed by xingkun")
    print("Version: 1.0")
    file_path = input('Please input file path:')
    # data = pd.read_excel(path)
    # file_path = 'friend2.7(1).xlsx'
    data = pd.read_excel(file_path)
    current_sheet = data.values.tolist()
    class_num_list = []
    end_class_num = 1
    for i in current_sheet:
        if i[0] != end_class_num:
            end_class_num = end_class_num + 1
    # print(end_class_num)

    students_sum = 0

    for i in range(end_class_num):
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                temp = []
                for m in j[3:]:
                    student_full_id = str(int(j[1]))
                    student_id = int(student_full_id[-2:])
                    print(j)
                    if not pd.isna(m) and int(m) != student_id:
                        temp.append(int(m))
                data.loc[line, 'sum'] = len(temp)
    # print(class_num_list)
    for i in range(end_class_num):
        totalPeople = 0
        sumHand = 0
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                totalPeople = totalPeople + 1
                sumHand = sumHand + data.loc[line, 'sum']
        for line, j in enumerate(current_sheet):
            if j[0] == i + 1:
                data.loc[line, '0/sum'] = sumHand / (totalPeople * (totalPeople - 1))
    data.to_excel(excel_writer=file_path, index=False, header=True)
