"""
@File: main-copy.py
@Author: Xingkun Zhang
@Email: 1475795322@qq.com
@Date: 2023/2/24 8:04
@Description:
"""

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print("Designed by xingkun")

# import xlrd
# data = xlrd.open_workbook_xls('firstcase.xlsx')
# table = data.sheets()[0]

import pandas as pd

data = pd.read_excel('firstcase_copy.xlsx')
print(data.head())
print("------------------")
print(data.columns)
print(data.index)
classId = 1
# for i in data.values.tolist():
# print(i)
# classId = i[0]
# studentId = str(i[1])
# print(studentId[6:len(studentId)])

sheetList = data.values.tolist()
for i in sheetList:
    if i[0] != classId:
        classId = classId + 1

print(classId)

for i in range(classId):
    print('current class %s' % (i + 1))
    m = []
    for j in sheetList:
        studentFullId = str(j[1])
        studentId = int(studentFullId[-2:])
        if j[0] == i + 1:
            if int(j[2]) != studentId and not pd.isna(j[2]):
                m.append(j[2])
            if int(j[3]) != studentId and not pd.isna(j[3]):
                m.append(j[3])
            if int(j[4]) != studentId and not pd.isna(j[4]):
                m.append(j[4])
    print(m)
    for line, j in enumerate(sheetList):
        if j[0] == i + 1:
            studentFullId = str(j[1])
            studentId = studentFullId[-2:]
            # print(studentId, ":", m.count(int(studentId)))
            # print(line, '受欢迎提名', m.count(int(studentId)))
            data.loc[line, '受欢迎提名'] = m.count(int(studentId))
    print("===================")
data.to_excel(excel_writer='firstcase_copy.xlsx', index=False)

data = pd.read_excel('firstcase_copy.xlsx')
sheetList = data.values.tolist()
print("----------------------")
for i in range(classId):
    totalPeople = 0
    totalSum = 0
    for line, j in enumerate(sheetList):
        if j[0] == i + 1:
            totalPeople = totalPeople + 1
            totalSum = totalSum + j[5]
    average = totalSum / totalPeople
    print(totalPeople, " ", totalSum, " ", average)
    # 离差平方和
    sumOfSquaresOfDeviations = 0
    for line, j in enumerate(sheetList):
        if j[0] == i + 1:
            sumOfSquaresOfDeviations = sumOfSquaresOfDeviations + pow(j[5] - average, 2)
    # 方差
    variance = sumOfSquaresOfDeviations / totalPeople
    # 标准差
    standardDeviation = pow(variance, 0.5)
    totalProtectSum = 0
    totalStandard = 0
    for line, j in enumerate(sheetList):
        if j[0] == i + 1:
            standard = (j[5] - average) / standardDeviation
            print('Z', standard)
            data.loc[line, 'Z班内受欢迎'] = standard
            if float(standard) > 0:
                if float(standard) > 0:
                    totalStandard = totalStandard + 1
                totalProtectSum = totalProtectSum + j[7]
            # data.loc[line, '受欢迎/保护'] = data.loc[line, '保护均分'] / standard
    for line, j in enumerate(sheetList):
        if j[0] == i + 1:
            data.loc[line, '受欢迎/保护'] = totalProtectSum / totalStandard
data.to_excel(excel_writer='firstcase_copy.xlsx', index=False)

# 保护均分
