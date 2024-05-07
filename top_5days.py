# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:24:08 2024

@author: Karthick
"""

from datetime import datetime
from datetime import timedelta
import talib
import os
import pathlib
import re
import pandas as pd
import warnings
import nselib

warnings.simplefilter(action='ignore', category=FutureWarning)

def get_date(d):
    yes_date = d-timedelta(days = 1)

    if yes_date not in leave:
        if yes_date.weekday() >=5:
            dat = get_date(yes_date)
        else:
            dat = yes_date
    else:
        dat = get_date(yes_date)
    
    return dat

def ema_filter(twnty,fifty,hunrd,twohund):
    
    if (twnty >= fifty) and (fifty >= hunrd) and (hunrd >=twohund):
        return 'EMA_ABV'
    else:
        return 'EMA_BLW'

folder = r'D:\Trade\TradingView'        
data_today = pd.DataFrame()
data_ystrday = pd.DataFrame()
data_dbystr = pd.DataFrame()
data_dbystr_m = pd.DataFrame()
data_dbystr_m2 = pd.DataFrame()
lv = nselib.trading_holiday_calendar()
leave = []
list_leave = list(lv[lv['Product']=='Equities']['tradingDate'])
for dt in list_leave:
    leave.append(datetime.strptime(dt, '%d-%b-%Y').date())


#leave = [datetime.date(2022,1,26),datetime.date(2022,5,3),datetime.date(2022,8,9),datetime.date(2022,8,11),datetime.date(2022,8,15),datetime.date(2022,8,31),datetime.date(2022,10,5),datetime.date(2022,10,26),datetime.date(2022,11,8),datetime.date(2023,1,26),datetime.date(2023,3,7),datetime.date(2023,3,30),datetime.date(2023,11,14),datetime.date(2023,11,27),datetime.date(2023,12,25),datetime.date(2024,1,22),datetime.date(2024,1,26),datetime.date(2024,3,22),datetime.date(2024,3,28),datetime.date(2024,4,11)]

dic_profit_shares = {}
dic_stck = {}
import datetime
end = datetime.date.today()
#end = end - timedelta(days = 3)

yes_date = get_date(end)
#yes_date = end - timedelta(days = 3)
start = get_date(yes_date)
#start = end - timedelta(days = 4)
start_m = get_date(start)
start_m2 = get_date(start_m)
print(start_m2,start_m,start,yes_date,end)

for f in os.listdir(folder):
    if str(end) in f:
        tmp_df1 = pd.read_csv(folder+ '/'+f)
        data_today = pd.concat([data_today,tmp_df1])
    elif str(yes_date) in f:
        tmp_df2 = pd.read_csv(folder+ '/'+f)
        data_ystrday = pd.concat([data_ystrday,tmp_df2])
    elif str(start) in f:
        tmp_df3 = pd.read_csv(folder+ '/'+f)
        data_dbystr = pd.concat([data_dbystr,tmp_df3])
    elif str(start_m) in f:
        tmp_df4 = pd.read_csv(folder+ '/'+f)
        data_dbystr_m = pd.concat([data_dbystr_m,tmp_df4])
    elif str(start_m2) in f:
        tmp_df5 = pd.read_csv(folder+ '/'+f)
        data_dbystr_m2 = pd.concat([data_dbystr_m2,tmp_df5])
        
dfs = [data_today,data_ystrday,data_dbystr,data_dbystr_m,data_dbystr_m2]

list_stcoks = []
for df in dfs:
    df.sort_values(by=['Change %'],ascending=False,inplace=True)
    top = df['Ticker'][:10]
    list_stcoks.extend(list(top))
smart_shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key) for key in list_stcoks})
pathlib.Path(r"D:\Trade\smart_list\top_smart_list" + end.strftime('%d%m%Y') +".txt").write_text(smart_shares_top_prior)

    