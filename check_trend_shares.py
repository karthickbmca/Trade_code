# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:51:27 2021

@author: KarthickB
"""

import pandas as pd
import datetime

dic_buy = {}

date1 = datetime.datetime(2020,8,17)
date2 = datetime.datetime(2021,8,17)
#date2 = '2021-06-23'
day = datetime.timedelta(days=1)

df_year = pd.read_excel(r'D:\Trade\Raw_data\data2021-08-17.xlsx')
df_year = df_year[['Date', 'Symbol', 'Open', 'High','Low', 'Close']]
df_year.drop_duplicates(inplace=True)
#df_year['type_candle'] = df_year.apply(lambda row: 'bull' if (row['Close'] > row['Open']) else 'bear', axis = 1)
list_stocks = df_year[df_year['Date'] == date2]['Symbol']
#list_stocks = ['FINPIPE']

for stock in list_stocks:
    try:
        df_stock = df_year[df_year['Symbol'] == stock]
        today_high = float(df_stock[(df_stock['Date'] == date2)]['Close'])
        today_low = float(df_stock[(df_stock['Date'] == date2)]['Open'])
        all_time_high = float(max(list(df_stock['Close'])))
        all_time_low = float(min(list(df_stock['Close'])))
        per_diff = (today_high - all_time_high) / all_time_high * 100
        date_hign = [pd.to_datetime(y) for y in list(df_stock[df_stock['Close'] == all_time_high]['Date'])]
        diff_day = [(pd.to_datetime(date2) - pd.to_datetime(x)).days for x in date_hign]
        if today_high > today_low:
            trend = 'Bull'
        else:
            trend = 'Bear'
            
        fcp = (all_time_high + all_time_low ) / 2
        fcp_perc = (today_high - fcp) / today_high * 100
        #check_trend = df_year[(df_year['Date'] == date_hign) & (df_year['Symbol'] == stock)]['type_candle']
        #check_trend = str(check_trend).split()[1]
        diff_day.sort()
        dic_buy[stock] = [diff_day,per_diff,date_hign,today_high,trend,fcp,fcp_perc,all_time_high,all_time_low]
                
    except:
        continue
dff = pd.DataFrame.from_dict(dic_buy, orient = 'index')

dff.columns = ['Difference','Perc','Date','High','Trend','fcp','fcp_perc','All_high','All_low']
dff.sort_values(by='Perc',inplace=True)
dff.to_excel(r'D:\Trade\Analysis\weekly_analysis_180821.xlsx')
    
            
        
        