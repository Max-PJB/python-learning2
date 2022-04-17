import pandas as pd
import numpy as np
import os
from pandas import DataFrame, Series
import re

df = pd.read_excel(r'C:\Users\Lenovo\Downloads\11.xlsx', sheet_name=0)  # 打开文件
print(df.columns)  # 查看列名
# print(df.dtypes)  # 查看各列数据类型所
print(df.head(20))  # 查看前20行数据
ck = df.iloc[:, 0]
je = df.loc[:,'合计金额']
print(ck.shape)
print('，'.join(ck))
print(sum(je))
