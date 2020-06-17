import pandas as pd 

df = pd.read_csv('04data.csv', encoding='cp932').groupby('時刻').mean()

# 指定カラムのデータを出力する(温度１と温度２がこの場合指定されている)
print(df.loc[:,'温度1(℃、x10)':'温度2(℃、x10)'])

# 下のprintは前からむのデータを出力する
# print(df)
