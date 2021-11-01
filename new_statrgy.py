# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:42:42 2021

@author: KarthickB
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-28.xlsx')

dic_buy = {}
#next_day = datetime(2021,5,31)
    
filter_date = datetime(2021,5,31)

list_stocks = list(data[(data['Date'] == filter_date)]['Symbol'])
#list_stocks = ['ICICIPRULI']
df_month = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\6_months_data2021-04-26.xlsx')

df_month = df_month[df_month['Date'] >= datetime(2021,2,1)]

df_week = df_month[df_month['Date'] >= datetime(2021,5,19)]

for syb in list_stocks:
    max_ = max(list(df_month[df_month['Symbol'] == syb]['High']))
    yest_va = float(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['High'])
    list_high = list(df_week['High'])
    result = max_ - yest_va
    if result < 0:
        dic_buy[syb] = [result,(result)/yest_va*100]
        
            
df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['result','perc']
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\new_stat_0206v2.xlsx')
