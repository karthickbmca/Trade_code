# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:44:15 2021

@author: -
"""

import pandas as pd

y_day = '2021-08-09'

today = '2021-08-10'

dic_profit_shares = {}

df = pd.read_excel(r'D:\Trade\Raw_data\data2021-08-10.xlsx')

stocks = list(df[df['Date'] == today]['Symbol'])

for e_st in stocks:
    try:
        yes_clos = int(df[(df['Date'] == y_day) & (df['Symbol'] == e_st)]['Close'])
        tod_close = int(df[(df['Date'] == today) & (df['Symbol'] == e_st)]['Close'])
        result = tod_close - yes_clos
        if result < 0:
            perc = (result / yes_clos) * 100
            dic_profit_shares[e_st] = [perc,yes_clos,tod_close,result]
    except:
        continue
    
df_profit = pd.DataFrame.from_dict(dic_profit_shares, orient = 'index')
df_profit.columns = ['perc','yes_clos','tod_close','result']
df_profit.sort_values(by='perc', ascending=False,inplace=True)
df_profit.to_excel(r'D:\Trade\Analysis\loss_share_100821.xlsx')
    