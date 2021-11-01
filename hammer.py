# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:31:36 2021

@author: KarthickB
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:58:05 2021

@author: -
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

for syb in list_stocks:
    try:
        max_ = max(list(df_month[df_month['Symbol'] == syb]['High']))
        min_ = min(list(df_month[df_month['Symbol'] == syb]['Low']))
        find_center_point = (max_ + min_)/2
        today = float(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['Close'])
        '''
        yest_va = int(data[(data['Date'] == filter_date) & (data['Symbol'] == syb)]['High'])
        today = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Close'])
        open_value = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['Open'])
        High = int(data[(data['Date'] == next_day) & (data['Symbol'] == syb)]['High'])
        result = today - yest_va
        #dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value,High]
        '''
        
        if find_center_point > today:
            dic_buy[syb] = ['less_fcp',today]
        else:
            dic_buy[syb] = ['high_fcp', today]

    except:
        continue

df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['fcp','today_value']
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\fcp010621.xlsx')