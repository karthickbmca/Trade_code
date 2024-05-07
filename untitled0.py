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
import pandas_ta as ta
import os
import pathlib
import re
import pandas as pd
import nselib
from nselib import capital_market
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


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

def comma(val):
    if ',' in val:
        return val.replace(',','')
    else:
        return val
        
data = pd.DataFrame()
leave = [datetime.date(2022,1,26),datetime.date(2022,5,3),datetime.date(2022,8,9),datetime.date(2022,8,11),datetime.date(2022,8,15),datetime.date(2022,8,31),datetime.date(2022,10,5),datetime.date(2022,10,26),datetime.date(2022,11,8),datetime.date(2023,1,26),datetime.date(2023,3,7),datetime.date(2023,3,30),datetime.date(2023,11,14),datetime.date(2023,11,27),datetime.date(2023,12,25),datetime.date(2024,1,22),datetime.date(2024,1,26)]

dic_profit_shares = {}
dic_stck = {}
end = datetime.date.today()
#end = end - timedelta(days = md)

yes_date = get_date(end)
#yes_date = end - timedelta(days = 3)
start = get_date(yes_date)
#start = end - timedelta(days = 4)
print(start,yes_date,end)
    #yes_date = yes_date + timedelta(days = 2)
#yes_date = datetime.date(2023,11,10)
#start = datetime.date(2023,11,9)
#end = datetime.date(2023,11,12)
#nse = Nse()
#q = nse.get_quote('infy')
all_stock_codes = nselib.capital_market.equity_list()['SYMBOL']
for stock in all_stock_codes:
    try:
        print(stock)
        df_data = capital_market.price_volume_and_deliverable_position_data(symbol=stock, from_date=start.strftime('%d-%m-%Y'), to_date=end.strftime('%d-%m-%Y'))
        df_data['type_candle'] = df_data.apply(lambda row: 'bull' if (row['ClosePrice'] > row['OpenPrice']) else 'bear', axis = 1)
        data = pd.concat([data,df_data]) 
    except:
        continue
data.rename(columns = {'OpenPrice':'Open','HighPrice':'High','LowPrice':'Low','ClosePrice':'Close'},inplace=True)
data['Date'] = pd.to_datetime(data.Date, format='%d-%b-%Y')
chnge_list = ['Open','High','Low','Close']
for chg in chnge_list:
    
    data[chg] = data[chg].replace(',', '', regex=True)
    data[chg] = data[chg].astype(float)
#data['High'] = data['High'].astype(float)
#data['Low'] = data['Low'].astype(float)
#data['Close'] = data['Close'].astype(float)

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
list_spntop = list(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['spinng_top'] != 0) ]['Symbol'])
#df_spintop.to_excel("D:\Trade\Analysis\\data_spingtop" + end.strftime('%Y-%m-%d') + ".xlsx")

stocks = list(data[data['Date'] ==  end.strftime('%Y-%m-%d')]['Symbol'])
print('Total stocks for today' + str(len(stocks)))

#yes_date = datetime.date(2022,3,2)
for e_st in stocks:
    try:
        yes_clos = float(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Close'])
        tod_close = float(data[(data['Date'] ==  end.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Close'])
        yes_open = float(data[(data['Date'] == yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Open'])
        tod_open = float(data[(data['Date'] == end.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Open'])
        dbf_open = float(data[(data['Date'] == start.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Open'])
        dbf_close = float(data[(data['Date'] == start.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['Close'])
        
        result = tod_close - yes_clos
        result1 = yes_clos - dbf_close
        
        if (result >= 0) and (str(data[(data['Date'] ==  end.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['type_candle']).split()[1] == 'bear'):
            idx = str(data[(data['Date'] ==  end.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['type_candle']).split()[0]
            data.at[int(idx),'type_candle'] =  'bull'
            #print('today check',e_st)
            
        if (result1 >= 0) and (str(data[(data['Date'] ==  yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['type_candle']).split()[1] == 'bear'):
            idx1 = str(data[(data['Date'] ==  yes_date.strftime('%Y-%m-%d')) & (data['Symbol'] == e_st)]['type_candle']).split()[0]
            data.at[int(idx1),'type_candle'] =  'bull'
            #print('yes_check',e_st)
            
        
        if result >= 0:
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
      
uniq_spn_top = set(list_spntop)-set(list_today_stock)                                                                           
df_profit = pd.DataFrame.from_dict(dic_profit_shares, orient = 'index')
df_profit.columns = ['perc','yes_clos','tod_close','result','Morn_star','Bull_eng']
df_profit.sort_values(by='perc', ascending=False,inplace=True)
sample_data = pd.read_csv('D:\Trade\Analysis\Equity.csv')
data_eq = sample_data[['Security Id','ISubgroup Name']]
data_eq['Security Id'] = data_eq['Security Id'].astype(str)
df_profit.to_excel(r'D:\Trade\Analysis\profit_share_' + end.strftime('%d%m%Y') +'.xlsx')
get_profit_data = pd.read_excel(r'D:\Trade\Analysis\profit_share_' + end.strftime('%d%m%Y') +'.xlsx')
get_profit_data.columns = ['Security Id','perc','yes_clos','tod_close','result','Morn_star','Bull_eng']
df_get_less_percent = get_profit_data[(get_profit_data['perc'] >=0) & (get_profit_data['perc'] <=1) & (get_profit_data['tod_close'] <=1000)]
list_less_one = df_get_less_percent['Security Id'].tolist()
get_profit_data['Security Id'] = get_profit_data['Security Id'].astype(str)
get_sector = get_profit_data.merge(data_eq,on =['Security Id'],how='left')[['Security Id','ISubgroup Name']]
print(get_sector.groupby('ISubgroup Name').count().sort_values(by = ['Security Id'], ascending=False))

df_two = pd.DataFrame.from_dict(dic_two, orient = 'index')
df_two.columns = ['perc_today','perc_yesterday','result']
df_two.sort_values(by='perc_today', ascending=False,inplace=True)
df_two.to_excel(r'D:\Trade\Analysis\profit_share_two_days' + end.strftime('%d%m%Y') +'.xlsx')
print('profit data is stored for today---' + end.strftime('%Y-%m-%d') )   

data_year = pd.read_excel("D:\Trade\Raw_data\\data_oneYear_EMA.xlsx")
data_today = pd.read_excel("D:\Trade\Raw_data\\data"+end.strftime('%Y-%m-%d')+ ".xlsx")
df_profit_two_days = pd.read_excel("D:\Trade\Analysis\profit_share_two_days"+end.strftime('%d%m%Y')+ ".xlsx")
df_profit_two_days.columns = ['Stocks','perc_today','perc_yesterday','result']
data_today = data_today[data_today['Date'] == end.strftime('%Y-%m-%d')]
data_y = pd.concat([data_year,data_today])
data_y = data_y.reset_index(drop=True)
stock = df_profit_two_days['Stocks'].tolist()
for stck in stock:
    try:
        slice_data = data_y[data_y['Symbol'] == stck]
        twenty_ema = ta.ema(slice_data['Close'],length=20).to_list()[-1]
        fifty_ema = ta.ema(slice_data['Close'],length=50).to_list()[-1]
        hundred_ema = ta.ema(slice_data['Close'],length=100).to_list()[-1]
        two_hund_ema = ta.ema(slice_data['Close'],length=200).to_list()[-1]
        #ten_ma = ta.ma(slice_data['Close'],length=10).to_list()[-1]
        dic_stck[stck] = [twenty_ema,fifty_ema,hundred_ema,two_hund_ema]
    except:
        continue
    
df_emas = pd.DataFrame.from_dict(dic_stck, orient = 'index')
df_emas.to_excel("D:\Trade\Analysis\\data_ema" + end.strftime('%Y-%m-%d') + ".xlsx")
data = pd.read_excel(r'D:\Trade\Analysis\\data_ema' + end.strftime('%Y-%m-%d') + '.xlsx')
data.columns = ['Stocks','20EMA','50EMA','100EMA','200EMA']
total_data = df_profit_two_days.merge(data,on = ['Stocks'],how = 'left')
total_data['ema_perc'] = (total_data['result']-total_data['200EMA'])/total_data['result']*100
total_data['ema_flag'] = total_data['ema_perc'].apply(lambda row :'True' if row > -1 else 'False')
total_data.to_excel(r'D:\Trade\Analysis\profit_share_two_days_ema' + end.strftime('%d%m%Y') +'.xlsx',index=False)
#filt_data = total_data[total_data['ema_flag'] == 'True']
filt_data = total_data.sort_values(by='perc_today')
list_ema_stocks = filt_data['Stocks'].tolist()
less_than_one_perc = set(list_less_one).union(set(list_ema_stocks))
shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in less_than_one_perc})
str_list = ','.join(shares_top_prior)
str_uniq_spn_top = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in uniq_spn_top})
fil_dic = {'NSE:'+re.sub('[&-]','_',key):val for key,val in dic_profit_shares.items() if val[2]<=1000}
profit_list = ','.join(dict(sorted(fil_dic.items(), key = lambda x: x[1][0], reverse = False)).keys())
pathlib.Path(r"D:\Trade\2_days_ema\list_stocks" + end.strftime('%d%m%Y') +".txt").write_text(shares_top_prior)
pathlib.Path(r"D:\Trade\profit_list\profit_stocks" + end.strftime('%d%m%Y') +".txt").write_text(profit_list)
pathlib.Path(r"D:\Trade\spn_top\spn_top" + end.strftime('%d%m%Y') +".txt").write_text(str_uniq_spn_top)
if os.path.exists('D:\Trade\Raw_data\\data_oneYear_EMA.xlsx'):
    os.remove('D:\Trade\Raw_data\\data_oneYear_EMA.xlsx')
data_y.to_excel('D:\Trade\Raw_data\\data_oneYear_EMA.xlsx',index=False)

stock = data_y['Symbol'].drop_duplicates().tolist()

interval = 4

dates = data_y['Date'].drop_duplicates().to_list()[-(interval):]

dates = dates[::-1]
#stock = ['UNOMINDA']
stc = []
for stck in stock:
    #print(stck)
    l=[]
    fil_stck = data_y[data_y['Symbol'] == stck]
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
   
watch_list = list(set(less_than_one_perc).union(set(stc))  )
watch_list = list(set(watch_list).union(set(list_spntop))  )
shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in watch_list})
smart_list = [] 
very_smart_list = []
for stock in watch_list:
    try:
        close = float(data_y[(data_y['Date'] ==  end.strftime('%Y-%m-%d')) & (data_y['Symbol'] == stock)]['Close'])
        slice_data = data_y[data_y['Symbol'] == stock]
        twenty_ema = ta.ema(slice_data['Close'],length=20).to_list()[-1]
        fif_ema = ta.ema(slice_data['Close'],length=50).to_list()[-1]
        hund_ema = ta.ema(slice_data['Close'],length=100).to_list()[-1]
        two_hund_ema = ta.ema(slice_data['Close'],length=200).to_list()[-1]
        ten_ma = ta.sma(slice_data['Close'],length=10).to_list()[-1]
        tight = (ten_ma - twenty_ema)/ten_ma*100
        if close >= twenty_ema:
            if twenty_ema >= fif_ema >= hund_ema>=two_hund_ema:
                smart_list.append(stock)
                
                if ((tight <=1) & (tight >= -1)) | (stock in less_than_one_perc):
                    very_smart_list.append(stock)
            
            #perc = ((close - twenty_ema) /close) * 100
            #if perc >= -1:
                
                
    except:
        continue
smart_shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in smart_list})
top_most_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in very_smart_list})

pathlib.Path(r"D:\Trade\watch_list\watch_list" + end.strftime('%d%m%Y') +".txt").write_text(shares_top_prior)
pathlib.Path(r"D:\Trade\smart_list\smart_list" + end.strftime('%d%m%Y') +".txt").write_text(smart_shares_top_prior)
pathlib.Path(r"D:\Trade\smart_list\very_smart_list" + end.strftime('%d%m%Y') +".txt").write_text(top_most_prior)
print('profit Stocks - '+str(len(fil_dic)))
print('watch list stocks - '+ str(len(watch_list)))
print('smart list stocks - '+ str(len(smart_list)))
print('very smart list stocks - '+ str(len(very_smart_list)))
