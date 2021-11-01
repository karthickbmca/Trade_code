# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:05:24 2021

@author: KarthickB
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:21:22 2021

@author: KarthickB
"""

import pandas as pd
#from datetime import datetime
import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-26oneweek.xlsx')

dic_buy = {}

date1 = datetime.datetime(2021,5,18)
date2 = datetime.datetime(2021,5,26)
day = datetime.timedelta(days=1)

while date1<=date2:
    
    list_stocks = list(data[(data['spinng_top'] != 0) & (data['Date'] == date1)]['Symbol'])
    
    
    for syb in list_stocks:
        try:
            high_value = float(data[(data['Symbol'] == syb) & (data['Date'] == date1)]['High'])
            latest_val = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Last'])
            df = data[(data['Symbol'] == syb) & (data['Date'] > date1)]
            if -100 in df['hammer'].tolist():
                dic_buy[syb] = [high_value,latest_val]
            
        except:
            continue
        '''
        if result > 0:
            try:
                dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value,High]
            except:
                continue
            
        '''
    date1 = date1 + day
         
    df = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df.columns = ['high','lastest']
#df.sort_values(by='per',inplace=True)
df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\hammer_check.xlsx')
        