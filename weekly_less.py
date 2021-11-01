# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:21:22 2021

@author: KarthickB
"""

import pandas as pd
#from datetime import datetime
import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-06-14.xlsx')

dic_buy = {}

date1 = datetime.datetime(2021,6,9)
date2 = datetime.datetime(2021,6,14)
vol_date = datetime.datetime(2021,6,14)
day = datetime.timedelta(days=1)

while date1<=date2:
    
    list_stocks = list(data[(data['spinng_top'] != 0) & (data['Date'] == date1)]['Symbol'])
    
    
    for syb in list_stocks:
        try:
            high_value = float(data[(data['Symbol'] == syb) & (data['Date'] == date1)]['High'])
            latest_val = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Last'])
            df = data[(data['Symbol'] == syb) & (data['Date'] > date1)]
            vol_df = data[(data['Symbol'] == syb) & (data['Date'] > vol_date)]
            avg_volume = vol_df['Volume'].mean()
            max_value = max(df['High'].tolist())
            result = high_value - max_value
            if result > 0:
                per = (high_value-latest_val)/latest_val*100
                dic_buy[syb] = [date1,high_value,max(df['High'].tolist()),latest_val,per,avg_volume]
            
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

df.columns = ['Date','High','next_high','today_close_value','per','Avg']
df.sort_values(by='per',inplace=True)
df.to_excel(r'D:\Trade\Raw_data\weekly_check_150621.xlsx')
        