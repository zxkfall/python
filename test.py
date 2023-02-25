"""
@File: test.py
@Author: Xingkun Zhang
@Email: 1475795322@qq.com
@Date: 2023/2/24 3:29
@Description: 
"""
from numpy import *
num = [[1, 2], [2, 3]]
mm = mat(num)
print(mm)
print("--------")
result = mm.tolist()
print(result)
result[0] = 1
print("--------")
print(result)
print("--------")
print(mm)

