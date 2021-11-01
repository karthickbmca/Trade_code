# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:46:33 2021

@author: -
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\6_months_data2021-04-23.xlsx')

dic_buy = {}

next_day = datetime(2021,4,9)

filter_date = datetime(2021,4,8)

list_stocks = list(data[(data['spinng_top'] != 0) & (data['Date'] == filter_date)]['Symbol'])

data_nday = data[data['Date'] == next_day]

for syb in list_stocks:
    try:
        today_top = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['spinng_top'])
        if today_top != 0:
            yest_va = int(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['High'])
            today = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Close'])
            result = today - yest_va
            if result > 0:
                dic_buy[syb] = [today,'check']
    except:
        continue

df = pd.DataFrame.from_dict(dic_buy, orient = 'index')
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\stock_to_buy_spn_conc_.xlsx')
            

