# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 19:32:35 2021

@author: KarthickB
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-06-04.xlsx')

dic_buy = {}
next_day = datetime(2021,6,3)
    
filter_date = datetime(2021,6,2)

list_stocks = list(data[(data['cdldoji'] != 0) & (data['Date'] == filter_date)]['Symbol'])

data_nday = data[data['Date'] == next_day]

for syb in list_stocks:
    try:
        df = data[(data['Symbol'] == syb) & (data['Date'] == next_day)]
        open_ = float(df['Open'])
        close_ = float(df['Close'])
        result = close_ - open_
        if result > 0:
            try:
                 dic_buy[syb] = [(result / open_) * 100]
            except:
                continue
            
    except:
        continue
    
    
df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['perc']
df = df.sort_values(by = 'perc', ascending = False)
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\doji05062021.xlsx')