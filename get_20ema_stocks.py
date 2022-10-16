# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:15:52 2022

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
end = end - timedelta(days = 2)

data_year = pd.read_excel("E:\Trade\Raw_data\\data_oneYear_EMA.xlsx")
nse = Nse()
l = []
all_stock_codes = nse.get_stock_codes() 
for stock in all_stock_codes:
    try:
        close = float(data_year[(data_year['Date'] ==  end.strftime('%Y-%m-%d')) & (data_year['Symbol'] == stock)]['Close'])
        slice_data = data_year[data_year['Symbol'] == stock]
        twenty_ema = ta.ema(slice_data['Close'],length=20).to_list()[-1]
        fif_ema = ta.ema(slice_data['Close'],length=50).to_list()[-1]
        hund_ema = ta.ema(slice_data['Close'],length=100).to_list()[-1]
        two_hund_ema = ta.ema(slice_data['Close'],length=200).to_list()[-1]
        if close >= twenty_ema:
            if twenty_ema >= fif_ema >= hund_ema>=two_hund_ema:
                l.append(stock)
            #perc = ((close - twenty_ema) /close) * 100
            #if perc >= -1:
                
                
    except:
        continue
    
str_list = ','.join(l)
pathlib.Path(r"E:\Trade\2_days_ema\list_stocks_20_50_100_200_EMA_"+str(end)+".txt").write_text(str_list)

            