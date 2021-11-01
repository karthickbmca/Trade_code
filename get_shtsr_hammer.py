# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:11:51 2021

@author: KarthickB
"""

import pandas as pd


df = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-04-26.xlsx')
df1 = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-04-27.xlsx')
df2 = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-04-28.xlsx')

df_all = pd.concat([df,df1,df2])

df_all = df_all.drop_duplicates()

dic_value = {}
for stock, df_i in df_all.groupby(by = 'Symbol'):
    set_sht_str = [int(int(x)-int(max(df_i['Low'].tolist()))) for x in df_i['Low'].tolist()]
    if sum(set_sht_str) < 2:
        dic_value[stock] = set_sht_str