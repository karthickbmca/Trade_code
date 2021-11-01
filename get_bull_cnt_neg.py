# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:59:48 2021

@author: KarthickB
"""

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-06-11_onemonth.xlsx')

dic_buy = {}

date1 = datetime.datetime(2021,6,4)
date2 = datetime.datetime(2021,6,11)
day = datetime.timedelta(days=1)


    
list_stocks = list(data[data['Date'] == date2]['Symbol'])
#list_stocks = ['AARTIIND']

def get_before_data(stock_date, df_f):

    old_date = stock_date - day
    df = df_f[df_f['Date'] == old_date]
    df_close = float(df['Close']) - float(df['Open'])
    if df_close > 0:
        return df_close/df['Open']*100
    else:
        get_before_data(old_date, df_f)
        return df_close/df['Open']*100
    
for syb in list_stocks:
    
    initial_open = float(data[(data['Symbol'] == syb) & (data['Date'] == date1)]['Open'])
    end_open = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Open'])
    Close = float(data[(data['Symbol'] == syb) & (data['Date'] == date2)]['Close'])
    df = data[(data['Symbol'] == syb) & (data['Date'] >= date1)]
    df = df.sort_values(by = 'Date')
    list_open_price = df['Open'].tolist()
    list_diff = []
    end_result = Close - end_open
    for idx_list_open in range(len(list_open_price)-1):
        diff = list_open_price[idx_list_open+1]-list_open_price[idx_list_open]
        list_diff.append(diff)
    pos = len(list(filter(lambda x:x>0,list_diff)))
    neg = len(list(filter(lambda x:x<0,list_diff)))
    if pos > neg:
        dic_buy[syb] = ['Up',Close]
    else:
        if list_diff[-1] > 0 and end_result > 0:
            dic_buy[syb] = ['Change_trend',Close]
        elif neg >= 4:
            if list_diff[-1] > 0:
                dic_buy[syb] = ['4 neg pos',Close]
            else:
                dic_buy[syb] = ['4 neg',Close]
        else:
            dic_buy[syb] = ['Down',Close]
            
            
            
df_f = pd.DataFrame.from_dict(dic_buy, orient = 'index')

df_f.columns = ['Trend','Close']
df_f.to_excel(r'C:\Users\KarthickB\Desktop\Trade\trend_1206.xlsx')
        