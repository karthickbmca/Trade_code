# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nsetools import Nse
from nsepy import get_history
import datetime
import numpy as np
from datetime import timedelta
import talib

import pandas as pd

def isdoji(opn,clos):
    res = (clos - opn)/clos * 100
    return res

def is_bearish(opn,clos):
    if opn > clos:
        return True
    else:
        return False
    
def is_bull(opn,clos):
    if clos > opn:
        return True
    else:
        return False
   
def is_bullish_candle(opn, clse):
    
    return clse > opn

def is_bearsh_cand(opn, clse):
    
    return clse < opn

    
def morning_star(tod_open,tod_close,dbf_open,dbf_close,yes_open,yes_clos):
     val_doji = isdoji(yes_open,yes_clos)
     if int(val_doji) == 0:
        check_bear = is_bearish(dbf_open,dbf_close)
        if check_bear == True:
            check_bull = is_bull(tod_open,tod_close)
            if check_bull == True:
                return True
     else:
        return False

def is_bullish_eng(tod_open,tod_close,yes_open,yes_clos):
    
    if is_bearsh_cand(yes_open,yes_clos):
        if (tod_close > yes_open) and (tod_open < yes_clos):
            return True
    
    
data = pd.DataFrame()
dic_profit_shares = {}

end = datetime.date.today()
#end = end - timedelta(days = 1)
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
nse = Nse()
#q = nse.get_quote('infy')
all_stock_codes = nse.get_stock_codes() 
for stock in all_stock_codes:
    try:
        print(stock)
        df_data = get_history(symbol = stock, start = start, end = end)
        df_data['type_candle'] = df_data.apply(lambda row: 'bull' if (row['Close'] > row['Open']) else 'bear', axis = 1)
        data = data.append(df_data) 
    except:
        continue
data['spinng_top'] = talib.CDLSPINNINGTOP(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data['hanging_man'] = talib.CDLHANGINGMAN(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data['hammer'] = talib.CDLHANGINGMAN(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data['shoot_star'] = talib.CDLSHOOTINGSTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data['inv_hammer'] = talib.CDLINVERTEDHAMMER(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data["cdlthrusting"]=talib.CDLTHRUSTING(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data['Dragon_fly'] = talib.CDLDRAGONFLYDOJI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# data["cdldoji"]=talib.CDLDOJI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
# file_name = 'data' + str(end)[:10]

#df = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-21oneweek.xlsx')
#data = data.append(df)
#data = data[['Symbol', 'Open', 'High', 'Low', 'Close', 'type_candle']]
data.to_excel("D:\Trade\Raw_data\\data" + end.strftime('%Y-%m-%d') + ".xlsx")
print('data is stored for today---' + end.strftime('%Y-%m-%d') )
data = pd.read_excel(r'D:\Trade\Raw_data\\data' + end.strftime('%Y-%m-%d') + '.xlsx')
df_spintop = data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['spinng_top'] != 0) ]
df_spintop.to_excel("D:\Trade\Analysis\\data_spingtop" + end.strftime('%Y-%m-%d') + ".xlsx")

stocks = list(data[data['Date'] ==  end.strftime('%Y-%m-%d')]['Symbol'])
print('Total stocks for today' + str(len(stocks)))

for e_st in stocks:
    try:
        yes_clos = float(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Close'])
        tod_close = float(data[(data['Date'] ==  end.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Close'])
        yes_open = float(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Open'])
        tod_open = float(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Open'])
        dbf_open = float(data[(data['Date'] == start.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Open'])
        dbf_close = float(data[(data['Date'] == start.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Close'])
        
        result = tod_close - yes_clos
        if result > 2:
            res_morning_star = morning_star(tod_open,tod_close,dbf_open,dbf_close,yes_open,yes_clos)
            res_bull_eng = is_bullish_eng(tod_open,tod_close,yes_open,yes_clos)
            perc = (result / yes_clos) * 100
            dic_profit_shares[e_st] = [perc,yes_clos,tod_close,result,res_morning_star,res_bull_eng]
    except:
        continue
list_today_stock = list(data[(data['Date'] ==  end.strftime('%Y-%m-%d')) & (data['type_candle'] ==  'bull')]['Symbol'])
list_yest_stock = list(data[(data['Date'] ==  yes_date.strftime('%Y-%m-%d')) & (data['type_candle'] ==  'bull')]['Symbol'])
two_day_stock = list(set(list_today_stock) & set(list_yest_stock))
dic_two = {}
for stc in two_day_stock:
    try:
        yes_clos = int(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == stc)]['Close'])
        yes_open = int(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == stc)]['Open'])
        perc_yes =  (yes_clos - yes_open)/yes_clos * 100
        tod_clos = int(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == stc)]['Close'])
        tod_open = int(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == stc)]['Open'])
        perc_tod =  (tod_clos - tod_open)/tod_clos * 100
        if tod_clos < 1000:
            dic_two[stc] = [perc_tod,perc_yes,tod_clos]
    except:
        continue
    
                                                                           
df_profit = pd.DataFrame.from_dict(dic_profit_shares, orient = 'index')
df_profit.columns = ['perc','yes_clos','tod_close','result','Morn_star','Bull_eng']
df_profit.sort_values(by='perc', ascending=False,inplace=True)
df_profit.to_excel(r'D:\Trade\Analysis\profit_share_' + end.strftime('%d%m%Y') +'.xlsx')
df_two = pd.DataFrame.from_dict(dic_two, orient = 'index')
df_two.columns = ['perc_today','perc_yesterday','result']
df_two.sort_values(by='perc_today', ascending=False,inplace=True)
df_two.to_excel(r'D:\Trade\Analysis\profit_share_two_days' + end.strftime('%d%m%Y') +'.xlsx')
print('profit data is stored for today---' + end.strftime('%Y-%m-%d') )   

