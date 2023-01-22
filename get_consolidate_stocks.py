# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:52:34 2022

@author: User
"""

import datetime
import numpy as np
from datetime import timedelta
import talib
import pandas as pd
import os
import re
import pathlib

data_year = pd.read_excel("E:\Trade\Raw_data\\data_oneYear_EMA.xlsx")
end = datetime.date.today()
stock = data_year['Symbol'].drop_duplicates().tolist()

interval = 4

dates = data_year['Date'].drop_duplicates().to_list()[-(interval):]

dates = dates[::-1]
#stock = ['UNOMINDA']
stc = []
for stck in stock:
    #print(stck)
    l=[]
    fil_stck = data_year[data_year['Symbol'] == stck]
    try:
        for d in range(len(dates)):
            if d < interval-1:
                cls1  = float(fil_stck[fil_stck['Date'] ==  dates[d].strftime('%Y-%m-%d')]['Close'])     
                cls2  = float(fil_stck[(fil_stck['Date'] ==  dates[d+1].strftime('%Y-%m-%d'))]['Close'])
                spn_top = int(fil_stck[fil_stck['Date'] ==  dates[d].strftime('%Y-%m-%d')]['spinng_top'])
                res = cls1-cls2
                perc=res/cls2*100
                if ( 1 >= perc >= -1) | (spn_top !=0):
                    l.append(perc)
                
        if len(l) >= 3 and cls1 <=1000:
            print(stck)
            stc.append(stck)
    except:
        pass        
    
    
shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in stc})
pathlib.Path(r"E:\Trade\consolidated_stocks\consolidated_stocks" + end.strftime('%d%m%Y') +".txt").write_text(shares_top_prior)