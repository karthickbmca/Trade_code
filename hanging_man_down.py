# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:57:10 2021

@author: -
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-04-26.xlsx')

dic_buy = {}
next_day = datetime(2021,4,26)

filter_date = datetime(2021,4,23)

list_stocks = list(data[(data['hanging_man'] != 0) & (data['Date'] == filter_date)]['Symbol'])

data_nday = data[data['Date'] == next_day]

for syb in list_stocks:
    try:
        max_ = max(list(data[data['Symbol'] == syb]['High']))
        min_ = min(list(data[data['Symbol'] == syb]['Low']))
        find_center_point = (max_ + min_)/2
        yest_va = int(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['High'])
        today = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Close'])
        open_value = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Open'])
        result = today - yest_va
    except:
        continue
    if result < 0 and open_value < find_center_point:
        dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value]
        

    df = pd.DataFrame.from_dict(dic_buy, orient = 'index')
    df.columns
    df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\stock_to_buy_withminmax_hanging.xlsx')