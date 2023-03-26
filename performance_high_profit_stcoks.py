# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:02:41 2023

@author: User
"""

import pandas as pd
import numpy as np
from datetime import timedelta
import datetime
import pandas_ta as ta
import os
import pathlib
import re
from nsepy import get_history

d= {}
path = 'E:\Trade\Analysis'
raw_date = pd.read_excel(r'E:\Trade\Raw_data\data_oneYear_EMA.xlsx')
#end = datetime.date.today()
#yes_date = end-timedelta(days = 1)
numdays = 20
#comp_data = raw_date[raw_date['Date'] == yes_date] 
base = datetime.datetime.today()
date_list = [(base - datetime.timedelta(days=x)).strftime('%d%m%Y') for x in range(numdays)]
from datetime import datetime
for da in date_list[::-1]:
    try:
        df = pd.read_excel(path+'/profit_share_'+da+'.xlsx')
        
        lis = df[df['perc'] >=19]['Unnamed: 0'].to_list()
        
        for l in lis:
            try:
                cls1 = float(df[(df['Unnamed: 0'] == l)]['tod_close'])
                lst = float(raw_date[(raw_date['Symbol'] == l) & (raw_date['Date'] == datetime.strptime(da,'%d%m%Y'))]['Last'])
                opn = float(raw_date[(raw_date['Symbol'] == l) & (raw_date['Date'] == datetime.strptime(da,'%d%m%Y'))]['Open'])
                   
                d[da +'-'+l] = [cls1]
            
            except:
                pass
    except:
        pass
    
df_emas = pd.DataFrame.from_dict(d, orient = 'index')
#df_emas.to_excel("E:\Trade\Analysis\\perf" + end.strftime('%Y-%m-%d') + ".xlsx")