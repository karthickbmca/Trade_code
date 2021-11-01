# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 09:13:34 2021

@author: KarthickB
"""

import pandas as pd
from datetime import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-28.xlsx')

dic_buy = {}
    
filter_date = datetime(2021,5,31)

list_stocks = list(data[(data['spinng_top'] != 0) & (data['Date'] == filter_date)]['Symbol'])

for syb in list_stocks:
    try:
        high = float(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['High'])
        
        dic_buy[syb] = [high]
    except:
        continue
        

df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['High']
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\stock_to_buy_check_010621.xlsx')