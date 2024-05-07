# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:22:18 2024

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
print(start_m,start,yes_date,end)

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
    
        
data_today['spinng_top'] = talib.CDLSPINNINGTOP(data_today['Open'].values, data_today['High'].values, data_today['Low'].values, data_today['Price'].values)
mutl_funds = list(data_today[data_today['Industry'] == 'Investment Trusts/Mutual Funds']['Ticker'])
cons_stcok = []
data_today['EMA_filter'] = data_today.apply(lambda ema:ema_filter(ema['Exponential Moving Average (20)'],ema['Exponential Moving Average (50)'],ema['Exponential Moving Average (100)'],ema['Exponential Moving Average (200)']),axis=1)
df_profit_today = data_today[(data_today['Change %'] > 0) & (data_today['EMA_filter'] == 'EMA_ABV')]['Ticker']
df_profit_ystrdy = data_ystrday[(data_ystrday['Change %'] > 0)]['Ticker']
two_days_profit = list(set(df_profit_today) & set(df_profit_ystrdy))
list_spn_top = data_today[(data_today['spinng_top'] != 0) & (data_today['EMA_filter'] == 'EMA_ABV')]['Ticker']
e_f = data_today[data_today['EMA_filter'] == 'EMA_ABV']['Ticker']
all_df = pd.concat([data_today,data_ystrday,data_dbystr,data_dbystr_m])
for stock in e_f:
    sliced = all_df[all_df['Ticker'] == stock]['Change %']
    i = 1
    for val in sliced:
        if ((val > -1) & (val < 1)):
            i = i + 1
        if i == 4:
            cons_stcok.append(stock)
            
smart_list = list(set(two_days_profit).union(set(list_spn_top)).union(set(cons_stcok)))
vry_smrt_list = [stck for stck in smart_list if stck not in mutl_funds]
smart_shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key) for key in vry_smrt_list})
pathlib.Path(r"D:\Trade\smart_list\very_smart_list" + end.strftime('%d%m%Y') +".txt").write_text(smart_shares_top_prior)

print('smart list stocks - '+ str(len(vry_smrt_list)))
grp_data = data_today[(data_today['Change %'] > 0) & (data_today['EMA_filter'] == 'EMA_ABV')].groupby('Industry')['Industry'].count().sort_values(ascending=False)
print(grp_data[:10])






