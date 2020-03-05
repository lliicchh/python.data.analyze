from pandas import DataFrame
from pandasql import sqldf

# pandas 基于 NumPy 构建的含有更高级数据结构和分析能力的工具包
# series 类似一维数据结构
# Data 类似数据库的表
# 数据清理：清理空数据，清理空格，数据格式转换等
# 数据统计：均值，方差...
# DataFrame 使用sql:
"""
# Series 数据结构
x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)
"""
# DataFrame 及 数据清理
data = {'Chinese': [66, 95, 93, 90, 80], 'English': [124, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data,
                index=['ZhangFei ', '$GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
# print(df1)
# print(df2)
"""
# 删除 列
df2 = df2.drop(columns=['Chinese'])
print(df2)
# 删除 行
df2 = df2.drop(index=["ZhangFei"])
print(df2)

# 改列名
df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace = True)
print(df2)

# 去掉重复的行
df2.drop_duplicates()

df2["Yingyu"].astype(np.int64)
df2["Yingyu"].astype('str')
print(df2)

#删除左右两边空格
df2['Chinese']=df2['Chinese'].map(str.strip)
#删除左边空格
df2['Chinese']=df2['Chinese'].map(str.lstrip)
#删除右边空格
df2['Chinese']=df2['Chinese'].map(str.rstrip)
def doubleDF(x):
    return 2*x
df1['Chinese'] = df1['Chinese'].apply(doubleDF)
print(df1)

"""

"""
# 数据统计
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
print(df1)
print(df1.describe())
"""

"""
# 数据合并
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})
# 按列合并
print(pd.merge(df1, df2, on="name"))

# 内连接
print(pd.merge(df1, df2, how="inner"))

# 左连接
print(pd.merge(df1, df2, how='left'))

# 右连接
print(pd.merge(df1, df2, how='right'))

# 外连接

print(pd.merge(df1, df2, how='outer'))
"""

# """
# DataFrame sql
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})

pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))
# """
