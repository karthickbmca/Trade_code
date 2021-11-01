# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:33:37 2021

@author: KarthickB
"""

import pandas as pd

data = pd.read_excel("D:\Trade\Raw_data\\data2021-08-03.xlsx")

y_day = '2021-08-02'

today = '2021-08-03'

dic_eng = {}

def is_bullish_candle(opn, clse):
    
    return clse > opn

def is_bearsh_cand(opn, clse):
    
    return clse < opn

def is_bullish_eng(syb):
    
    df_curr_day = data[(data['Date'] == today) & (data['Symbol'] == syb)]
    df_prv_day = data[(data['Date'] == y_day) & (data['Symbol'] == syb)]
    
    if is_bearsh_cand(float(df_prv_day['Open']) , float(df_prv_day['Close'])):
        if (float(df_curr_day['Close']) > float(df_prv_day['Open'])) and (float(df_curr_day['Open']) < float(df_prv_day['Close'])):
            return True
list_of_stocks = data[(data['Date'] == today)]['Symbol']       
for syb in list_of_stocks:
    try:
        result = is_bullish_eng(syb)
        if result == True:  
            print(syb)
            dic_eng[syb] = result
    except:
        continue        
    
        

    
        
    
    