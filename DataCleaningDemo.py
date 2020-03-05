# coding:utf-8

# 数据清理的例子

import pandas as pd
from pandas import Series, DataFrame
df= DataFrame(pd.read_excel('data/accountMessage.xlsx'))
# score.to_excel('data1.xlsx')
# print(df)


# 删除全空的行
df.dropna(how='all',inplace=True)
print(df)



