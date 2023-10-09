# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:40:14 2023

@author: User
"""

import pandas as pd
import pathlib
import re
import datetime
from datetime import timedelta
end = datetime.date.today()
#end = end - timedelta(days=3)
df = pd.read_excel(r'C:\Users\User\Downloads\NSE-STOCK-SECTOR-INDUSTRY (1).xlsx')
df = df.dropna(subset = ['SECTOR'])
sector = set(df.SECTOR.tolist())
d = {}
for each_Se in sector:
    tmp = df[df['SECTOR'] == each_Se]
    ind = set(tmp.INDUSTRY.tolist())
    for e_i in ind:
        name = each_Se.upper() + '_' + re.sub('\W+','_', e_i).title()
        tmp1 = tmp[df['INDUSTRY'] == e_i]
        sym = '+'.join(['NSE:' + x for x in tmp1.SYMBOL.tolist()][:10])
        if len(tmp1.SYMBOL.tolist()) < 10:
            d[name] = '(' + sym + ')/' + str(len(tmp1.SYMBOL.tolist()))
        else:
            d[name] = '(' + sym + ')/' + str(10)
        
    
df_screener = pd.DataFrame.from_dict(d, orient = 'index')    
df_screener.columns = ['stocks']
df_screener.to_csv(r'C:\Users\User\Downloads\sector_stocks.csv')
