# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:05:51 2021

@author: KarthickB
"""

import pandas as pd
#from datetime import datetime
import datetime

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-06-17.xlsx')

dic_buy = {}

date1 = datetime.datetime(2021,3,12)
date2 = datetime.datetime(2021,6,16)
day = datetime.timedelta(days=1)


    
list_stocks = list(data[data['Date'] == date1]['Symbol'])
#list_stocks = ['BCLIND']

    
    

for syb in list_stocks:
    try:
        initial_open = float(data[(data['Symbol'] == syb) & (data['Date'] == date1)]['Open'])
        end_open = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Open'])
        Close = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Close'])
        max_ = max(list(data[data['Symbol'] == syb]['High']))
        min_ = min(list(data[data['Symbol'] == syb]['Low']))
        vol = data[data['Symbol'] == syb]['Volume'].mean()
        find_center_point = (max_ + min_)/2
        df = data[(data['Symbol'] == syb) & (data['Date'] >= date1)]
        df = df.sort_values(by = 'Date')
        list_open_price = df['Open'].tolist()
        list_close_price = df['Close'].tolist()
        list_volume = df['Volume'].tolist()
        list_diff = []
        vol_up = 0
        vol_down = 0
        end_result = Close - end_open
        perc = float(end_result / end_open) * 100
        if perc < 1:
            curr_day_perc = perc
        else:
            curr_day_perc = perc
        per_fcp = (find_center_point - Close)/find_center_point*100
        if find_center_point < Close:
            fcp = 'Trend is above with ---' + str(per_fcp)
        else:
            fcp = 'Trend is below with ---' + str(per_fcp)
        for idx_list_open in range(len(list_open_price)):
            diff = list_close_price[idx_list_open]-list_open_price[idx_list_open]
            list_diff.append(diff)
            if list_volume[idx_list_open] < vol:
                vol_down = vol_down + 1
            else:
                vol_up = vol_up + 1
        pos = len(list(filter(lambda x:x>0,list_diff)))
        neg = len(list(filter(lambda x:x<0,list_diff)))
        if vol_down > vol_up:
            volu = 'Volume less'
        else:
            volu = 'Volume High'
        if pos > neg:
            list_close = df['Open'].tolist()
            list_close = list_close[len(list_close)-10:]
            for l in range(len(list_close)-1):
                if (list_close[l] - list_close[l+1]) > 0:
                    check_neg = False
                    
                else:
                    check_neg = True
                    break
            if check_neg == False:
                dic_buy[syb] = ['Up_continueneg',Close,fcp,volu,curr_day_perc]
            else:
                dic_buy[syb] = ['Up',Close,fcp,volu,curr_day_perc]
        else:

            list_close = df['Open'].tolist()
            list_close = list_close[len(list_close)-10:]
            for l in range(len(list_close)-1):
                if (list_close[l] - list_close[l+1]) > 0:
                    check_neg = False
                    
                else:
                    check_neg = True
                    break
            
            if check_neg == False:
                dic_buy[syb] = ['down_continueneg',Close,fcp,volu,curr_day_perc]
            else:
                dic_buy[syb] = ['down',Close,fcp,volu,curr_day_perc]
    except:
        
        continue
    
dff = pd.DataFrame.from_dict(dic_buy, orient = 'index')

dff.columns = ['Trend','Close','fcp','volume','Find_one_perc']
#df.sort_values(by='per',inplace=True)
dff.to_excel(r'C:\Users\KarthickB\Desktop\Trade\trend1706_v3.xlsx')
    