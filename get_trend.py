# -*- coding: utf-8 -*-

"""
Created on Sun May 30 21:07:07 2021

@author: KarthickB
"""

import pandas as pd
#from datetime import datetime
import datetime

data = pd.read_excel(r'D:\Trade\Raw_data\data2021-06-28_3year.xlsx')

dic_buy = {}

date1 = datetime.datetime(2021,6,22)
date2 = datetime.datetime(2021,6,28)
day = datetime.timedelta(days=1)


    
list_stocks = list(data[data['Date'] == date1]['Symbol'])
#list_stocks = ['BCLIND']

    
    

for syb in list_stocks:


    try:  
        initial_open = float(data[(data['Symbol'] == syb) & (data['Date'] == date1)]['Open'])
        end_open = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Open'])
        today_high = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['High'])
        Close = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Close'])
        max_ = max(list(data[data['Symbol'] == syb]['High']))
        min_ = min(list(data[data['Symbol'] == syb]['Low']))
        #vol = data[data['Symbol'] == syb]['Volume'].mean()
        find_center_point = (max_ + min_)/2
        df = data[(data['Symbol'] == syb) & (data['Date'] >= date1)]
        df = df.sort_values(by = 'Date')
        list_open_price = df['Open'].tolist()
        list_close_price = df['Close'].tolist()
        #list_volume = df['Volume'].tolist()
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
        pos = len(list(filter(lambda x:x>0,list_diff)))
        neg = len(list(filter(lambda x:x<0,list_diff)))
        if pos > neg:
            dic_buy[syb] = ['Up',Close,fcp,curr_day_perc,today_high]
        else:
            if neg >= 4:
                if end_result > 0:
                    dic_buy[syb] = ['4 neg pos',Close,fcp,curr_day_perc]
                else:
                    df['check_bearish'] = df.apply(lambda x: 'bear' if x['Close'] < x['Open'] else 'bull', axis = 1)
                    count_bearing = set(df['check_bearish'].tolist()[1:])
                    if len(count_bearing) == 1:
                        bear = 'yes'
                        list_close = df['Close'].tolist()
                        list_close = list_close[1:]
                        for l in range(len(list_close)-1):
                            if (list_close[l] - list_close[l+1]) > 0:
                                check_continue = True
                                
                            else:
                                check_continue = False
                                break
                    else:
                        bear = 'No'
                    if bear == 'yes' and check_continue == True:
                        dic_buy[syb] = ['4 neg continues',Close,fcp,curr_day_perc,today_high]
                    else:
                        dic_buy[syb] = ['4 neg',Close,fcp,curr_day_perc,today_high]
                    
            elif neg >= 3 and end_result >0:
                    dic_buy[syb] = ['3 neg pos',Close,fcp,curr_day_perc,today_high]
            else:
                dic_buy[syb] = ['Down',Close,fcp,curr_day_perc,today_high]
            

    except:
        continue
    
'''  
    if result > 0:
        try:
            dic_buy[syb] = [(result / yest_va) * 100,today,yest_va,find_center_point,open_value,High]
        except:
            continue
        
    '''
     
dff = pd.DataFrame.from_dict(dic_buy, orient = 'index')

dff.columns = ['Trend','Close','fcp','Find_one_perc','High']
#df.sort_values(by='per',inplace=True)
dff.to_excel(r'D:\Trade\Analysis\trend2906_v1.xlsx')
    