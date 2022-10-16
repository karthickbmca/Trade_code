# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:44:32 2022

@author: User
"""

from nsetools import Nse
from nsepy import get_history
import datetime
import numpy as np
from datetime import timedelta
#import talib
import pandas_ta as ta
import os
import pathlib
import pandas as pd
end = datetime.date.today()
import sys

if datetime.datetime.today().weekday() == 0:
    start = end - timedelta(days = 4)
elif datetime.datetime.today().weekday() == 1:
    start = end - timedelta(days = 4)
else:
    start = end - timedelta(days = 2)
    
    
if datetime.datetime.today().weekday() == 1:
    yes_date = end - timedelta(days = 1)
else:
    yes_date = start + timedelta(days = 1)
    
    
data = pd.read_excel(r'E:\Trade\Raw_data\\data' + end.strftime('%Y-%m-%d') + '.xlsx').drop_duplicates()
data_year = pd.read_excel("E:\Trade\Raw_data\\data_oneYear_EMA.xlsx")
stocks = list(set(data['Symbol'].tolist()))
d = {}
for es in stocks:
    try:
        #c_data = data[data['Symbol'] == es]
        yes_vol = float(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == es)]['Turnover'])
        before = float(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == es)]['Turnover'])
        cand = str(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == es)]['type_candle']).split()[1]
        res = ((yes_vol-before)/yes_vol)*100
        price = float(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == es)]['Last'])
        slice_data = data_year[data_year['Symbol'] == es]
        twenty_ema = ta.ema(slice_data['Close'],length=20).to_list()[-1]
        fifty_ema = ta.ema(slice_data['Close'],length=50).to_list()[-1]
        hundred_ema = ta.ema(slice_data['Close'],length=100).to_list()[-1]
        two_hund_ema = ta.ema(slice_data['Close'],length=200).to_list()[-1]
        dif_20 = (price-twenty_ema)/price*100
        dif_200 = round(float((price-two_hund_ema)/price*100),2)
        d[es] = [res,cand,twenty_ema,two_hund_ema,dif_20,dif_200,price]
       #dic_stck[stck] = [twenty_ema,fifty_ema,hundred_ema,two_hund_ema]
       
    except Exception as e:
        print(e)
        continue
df_two = pd.DataFrame.from_dict(d, orient = 'index')
df_two.columns = ['result','trend','20_actl','200_actl','diff_20','diff_200','price']
df_two.sort_values(by='result', ascending=False,inplace=True)
df_two.to_excel(r'E:\Trade\Analysis\check' + end.strftime('%d%m%Y') +'.xlsx')