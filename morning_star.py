# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 08:08:41 2021

@author: Karthik
"""

import pandas as pd
import datetime
from datetime import timedelta

end = datetime.date.today() - timedelta(days = 2)
if datetime.datetime.today().weekday() == 0:
    start = end - timedelta(days = 3)
else:
    start = end - timedelta(days = 1)


data1 = pd.read_excel(r'D:\Trade\Raw_data\data' + end.strftime('%Y-%m-%d') +'.xlsx')
data2 = pd.read_excel(r'D:\Trade\Raw_data\data' + start.strftime('%Y-%m-%d') +'.xlsx')
data = pd.concat([data1,data2])
data = data.drop_duplicates()
dic_buy = {}

today = end.strftime('%Y-%m-%d')
y_day = start.strftime('%Y-%m-%d')
day_bf_ystrday = (start - timedelta(days = 3)).strftime('%Y-%m-%d')

day = datetime.timedelta(days=1)



def isdoji(opn,clos):
    res = (clos - opn)/clos * 100
    return res

def is_bearish(opn,clos):
    if opn > clos:
        res = (opn - clos)/opn * 100
        return res,True
    else:
        return 0, False
    
def is_bull(opn,clos):
    if clos > opn:
        res = (clos - opn)/ clos * 100
        return res,True
    else:
        return 0, False
    
all_stocks = list(data[data['Date'] == today]['Symbol'])

    
for stock in all_stocks:
    try:
        val_doji = isdoji(float(data[(data['Date'] == y_day) & (data['Symbol'] == stock)]['Open']),
                       float(data[(data['Date'] == y_day) & (data['Symbol'] == stock)]['Close']))
        if int(val_doji) == 0:
            find_bear,check_bear = is_bearish(float(data[(data['Date'] == day_bf_ystrday) & (data['Symbol'] == stock)]['Open']),
                       float(data[(data['Date'] == day_bf_ystrday) & (data['Symbol'] == stock)]['Close']))
            if check_bear == True:
                find_bull,check_bull = is_bull(float(data[(data['Date'] == today) & (data['Symbol'] == stock)]['Open']),
                       float(data[(data['Date'] == today) & (data['Symbol'] == stock)]['Close']))
                        
                if check_bull == True:
                    dic_buy[stock] = [val_doji,find_bear,find_bull]
                    
    except:
        continue
    
dff = pd.DataFrame.from_dict(dic_buy, orient = 'index')
dff.columns = ['Doji_per','bear_perc','bull_perc']
dff.to_excel(r'D:\Trade\Analysis\morning_star_' + today + '.xlsx')