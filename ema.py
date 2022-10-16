# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:14:47 2022

@author: Karthik
"""

from nsetools import Nse
from nsepy import get_history
import datetime
import numpy as np
from datetime import timedelta
import os
import pandas_ta as ta

import pandas as pd
end = datetime.date.today()
dic_stck = {}
#end = end - timedelta(days = 2)

data_year = pd.read_excel("D:\Trade\Raw_data\\data_oneYear_EMA.xlsx")
df_profit_today = pd.read_excel("D:\Trade\\Analysis\\profit_share_"+end.strftime('%d%m%Y')+ ".xlsx")
df_profit_two_days = pd.read_excel("D:\Trade\Analysis\profit_share_two_days"+end.strftime('%d%m%Y')+ ".xlsx")
df_profit_two_days.columns = ['Stocks','perc_today','perc_yesterday','result']
df_profit_today.columns = ['Stocks','perc_today','yes_clos','tod_close','result','Morn_star','Bull_eng']
diff_stocks = set(df_profit_today['Stocks'].tolist()) - set(df_profit_two_days['Stocks'].tolist())
for stck in diff_stocks:
    try:
        slice_data = data_year[data_year['Symbol'] == stck]
        twenty_ema = ta.ema(slice_data['Close'],length=20).to_list()[-1]
        fifty_ema = ta.ema(slice_data['Close'],length=50).to_list()[-1]
        hundred_ema = ta.ema(slice_data['Close'],length=100).to_list()[-1]
        two_hund_ema = ta.ema(slice_data['Close'],length=200).to_list()[-1]
        dic_stck[stck] = [twenty_ema,fifty_ema,hundred_ema,two_hund_ema]
    except:
        continue
    
df_emas = pd.DataFrame.from_dict(dic_stck, orient = 'index')
df_emas.to_excel("D:\Trade\Analysis\\today_profit_ema" + end.strftime('%Y-%m-%d') + ".xlsx")
data = pd.read_excel(r'D:\Trade\Analysis\\today_profit_ema' + end.strftime('%Y-%m-%d') + '.xlsx')
data.columns = ['Stocks','20EMA','50EMA','100EMA','200EMA']
total_data = df_profit_today.merge(data,on = ['Stocks'],how = 'inner')
total_data['ema_perc'] = (total_data['tod_close']-total_data['200EMA'])/total_data['tod_close']*100
total_data['ema_flag'] = total_data['ema_perc'].apply(lambda row :'True' if row > -1 else 'False')
total_data.to_excel(r'D:\Trade\Analysis\profit_share_today_ema' + end.strftime('%d%m%Y') +'.xlsx',index=False)
'''
if os.path.exists('D:\Trade\Raw_data\\data_oneYear_EMA.xlsx'):
    os.remove('D:\Trade\Raw_data\\data_oneYear_EMA.xlsx')
data_y.to_excel('D:\Trade\Raw_data\\data_oneYear_EMA.xlsx',index=False)
'''