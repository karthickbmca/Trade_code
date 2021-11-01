# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:23:23 2021

@author: -
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\6_months_data2021-04-23.xlsx')

dic_buy = {}
next_day = datetime(2021,4,6)

filter_date = datetime(2021,4,7)

list_stocks = list(data[(data['spinng_top'] != 0) & (data['Date'] == filter_date)]['Symbol'])


for syb in list_stocks:
    try:
        max_ = max(list(data[data['Symbol'] == syb]['High']))
        min_ = min(list(data[data['Symbol'] == syb]['Low']))
        find_center_point = (max_ + min_)/2
        open_value = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Open'])
    
    except:
        continue
    if open_value < find_center_point:
        dic_buy[syb] = [find_center_point,open_value]
        

    df = pd.DataFrame.from_dict(dic_buy, orient = 'index')
    df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\sPINNG_TOP.xlsx')