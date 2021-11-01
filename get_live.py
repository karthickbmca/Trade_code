# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:33:59 2021

@author: KarthickB
"""

import requests
from bs4 import BeautifulSoup 
import pandas as pd
from win32com.client import Dispatch
from nsetools import Nse
speaker = Dispatch("SAPI.spVoice")
nse = Nse()
dic_stock_name = nse.get_stock_codes()
df = pd.read_excel(r'D:\Trade\Analysis\live_23092021.xlsx')

#df.rename(columns = {'Unnamed: 0':'Symbol'},inplace = True)
#list_stcoks = df[df['Trend'] == '4 neg continues']['Symbol'].tolist()
list_stcoks = df['Symbol'].tolist()
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
        try:
            high = float(df[df['Symbol'] == stock_symbol]['High'])
            stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_symbol)
            headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
            response = requests.get(stock_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            data_array = soup.find(id='responseDiv').getText().strip().split(":")
            for item in data_array:
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
                     low=data_array[index].split('"')[1]
                    
            opn = float(open_amt.replace(',',''))
            result = float(latestPrice.replace(',','')) - high
            if result > 0:
                print(stock_symbol)
            #per = result / opn * 100
            #per = round(per,2)
            
            #if result > 0:
            #speaker.Speak(dic_stock_name[stock_symbol] + ' is now Rupees' + latestPrice + ' with percentage ' + str(per))
                #dic_stocks[stock_symbol] = [latestPrice, high_price,dayHigh]

        except:
            continue

    
#df_live = pd.DataFrame.from_dict(dic_stocks, orient = 'index')
#df_live.columns = ['latestPrice', 'yest_high','dayHigh']
#df_live.to_excel(r'C:\Users\KarthickB\Desktop\Trade\live_0106_v2.xlsx')
            