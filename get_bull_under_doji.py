# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 01:53:58 2021

@author: Karthik
"""

import pandas as pd
import datetime

data = pd.read_excel(r'D:\Trade\Raw_data\data2021-06-30.xlsx')

dic_buy = {}

today = datetime.datetime(2021,6,29)
y_day = datetime.datetime(2021,6,28)
day_bf_ystrday = datetime.datetime(2021,6,24)

day = datetime.timedelta(days=1)



def isdoji(opn,clos):
    res = (clos - opn)
    return res

def is_bull(opn,clos):
    if opn < clos:
        res = (opn - clos)/opn * 100
        return res,True
    else:
        return 0, False
    
all_stocks = list(data[data['Date'] == today]['Symbol'])

    
for stock in all_stocks:
    try:
        val_doji = isdoji(float(data[(data['Date'] == y_day) & (data['Symbol'] == stock)]['Open']),
                       float(data[(data['Date'] == y_day) & (data['Symbol'] == stock)]['Close']))
        close_doji = float(data[(data['Date'] == y_day) & (data['Symbol'] == stock)]['Close'])
        if int(val_doji) == 0:
            val_bull,check = is_bull(float(data[(data['Date'] == today) & (data['Symbol'] == stock)]['Open']),
                       float(data[(data['Date'] == today) & (data['Symbol'] == stock)]['Close']))
            if check == True:
                open_bull = float(data[(data['Date'] == today) & (data['Symbol'] == stock)]['Close'])
                if close_doji > open_bull:
                    print(stock)
                    
    except:
        continue