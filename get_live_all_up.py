# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:08:48 2021

@author: KarthickB
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:33:59 2021

@author: KarthickB
"""

import requests
from bs4 import BeautifulSoup 
import pandas as pd
from multiprocessing import Pool
from multiprocessing import freeze_support

df = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\less_check070621.xlsx')

list_stcoks = list(df['Symbol'])

#list_stcoks  = ['orienthot']
dic_stocks = {}


        

# def scrape(url):
#     try:
#         headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         data_array = soup.find(id='responseDiv').getText().strip().split(":")
#         for item in data_array:
#             print(item)
#             if 'lastPrice' in item:
#                 index = data_array.index(item)+1
#                 latestPrice=data_array[index].split('"')[1]weekly_check_210521
#             elif 'open' in item:
#                 index = data_array.index(item)+1
#                 open_amt=data_array[index].split('"')[1]
#             elif 'closePrice' in item:
#                 index = data_array.index(item)+1
#                 close_amt=data_array[index].split('"')[1]
#             elif 'dayHigh' in item:
#                 index = data_array.index(item)+1
#                 dayHigh=data_array[index].split('"')[1]
                
#             elif 'symbol' in item:
#                 index = data_array.index(item)+1
#                 symbol=data_array[index].split('"')[1]
                
#             dic_stocks[symbol] = [latestPrice,open_amt,close_amt,dayHigh]
            
    
for _ in range(1):
    for stock_symbol in list_stcoks:
        
        print(stock_symbol)
        stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_symbol)
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        response = requests.get(stock_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data_array = soup.find(id='responseDiv').getText().strip().split(":")
        for item in data_array:
            try:
                if 'lastPrice' in item:
                    index = data_array.index(item)+1
                    latestPrice=data_array[index].split('"')[1]
                elif 'dayHigh' in item:
                     index = data_array.index(item)+1
                     dayHigh=data_array[index].split('"')[1]
                     
                     
                elif 'open' in item:
                     index = data_array.index(item)+1
                     open_amt=data_array[index].split('"')[1]
                     
                elif 'dayLow' in item:
                     index = data_array.index(item)+1
                     low = data_array[index].split('"')[1]
                     
                elif 'totalTradedVolume' in item:
                    index = data_array.index(item)+1
                    volume = data_array[index].split('"')[1]
                    
            except:
                continue
        
            #if (latestPrice - high_price) > 0:
        dic_stocks[stock_symbol] = [latestPrice,dayHigh,open_amt,low]
            
    
    
df_live = pd.DataFrame.from_dict(dic_stocks, orient = 'index')
df_live.columns = ['Close','t_High','Open','Low']
df_live['Date'] = df["Date"].values
df_live['High'] = df["High"].values
df_live['bef_high'] = df["bef_high"].values
df_live['perc'] = df["perc"].values
df_live.to_excel(r'C:\Users\KarthickB\Desktop\Trade\live_0706_6pm.xlsx')
            