# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:58:05 2021

@author: -
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-06-07.xlsx')

dic_buy = {}
next_day = datetime(2021,6,7)

filter_date = datetime(2021,6,4)

list_stocks = list(data[(data['spinng_top'] != 0) & (data['Date'] == filter_date)]['Symbol'])

data_nday = data[data['Date'] == next_day]

for syb in list_stocks:
    try:
        max_ = max(list(data[data['Symbol'] == syb]['High']))
        min_ = min(list(data[data['Symbol'] == syb]['Low']))
        find_center_point = (max_ + min_)/2
        yest_va = int(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['High'])
        today = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Close'])
        open_value = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Open'])
        High = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['High'])
        result = today - yest_va
        #dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value,High]
    except:
        continue
    
    if result < 0:
        try:
            dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value,High]
        except:
            continue
        

df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['perc','today_close','yes_High','fcp','today_open','High']
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\stock_to_buy_check_310521_LESS.xlsx')