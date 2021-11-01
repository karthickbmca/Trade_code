# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:16:35 2021

@author: KarthickB
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-28_onemonth.xlsx')

dic_buy = {}
next_day = datetime(2021,5,28)
    
filter_date = datetime(2021,5,27)

list_stocks = list(data[data['Date'] == filter_date]['Symbol'])

data_nday = data[data['Date'] == next_day]

for syb in list_stocks:
    try:
        max_ = max(list(data[data['Symbol'] == syb]['High']))
        min_ = min(list(data[data['Symbol'] == syb]['Low']))
        find_center_point = (max_ + min_)/2
        yest_va = float(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['    '])
        today = float(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Close'])
        open_value = float(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Open'])
        High = float(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['High'])
        low = float(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Low'])
        result = today - yest_va
    except:
        continue
    
    if result > 0 and low == open_value:
        try:
            dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value,High]
        except:
            continue
        

df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['perc','today_close','yes_High','fcp','today_open','High']
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\stock_check_all_2905v1.xlsx')