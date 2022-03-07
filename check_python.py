# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:47:24 2021

@author: Karthik
"""

import webbrowser
import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import re
from selenium import webdriver
import os

output_name = 'fundamental_analysis'

new_url = []
symbol_url = {}
url_link = pd.read_excel(r'D:\Trade\Analysis\money_control_url.xlsx')
profit_today = pd.read_excel(r'D:\Trade\Analysis\profit_share_25112021.xlsx')
print(profit_today.shape)
profit_today.rename(columns={'Unnamed: 0':'Symbol'},inplace=True)
url_symbol = url_link['SYMBOL'].tolist()
url_full = url_link['url'].tolist()
#driver = webdriver.Chrome(executable_path=r'C:\Users\Karthik\Downloads/chromedriver.exe')

for missing_symbol in profit_today['Symbol'].tolist():
    try:
        if missing_symbol in url_symbol:
            symbol_url[missing_symbol] = url_full[url_symbol.index(missing_symbol)]
        else:
            req = webbrowser.open_new('https://www.google.com/search?q='+missing_symbol+'+share+price')
            html_page = requests.get('https://www.google.com/search?q='+missing_symbol+'+share+price')
            soup = BeautifulSoup(html_page.content, "html.parser")
    
            #driver.get('https://www.google.com/search?q='+missing_symbol+'+share+price')
            
            for rs in soup.findAll('a'):
                try:
                    if type(rs.get('href')) == str:
                        if 'www.moneycontrol' in rs.get('href'):
                            url = str(rs.get('href')).split('=')[1]
                        else:
                            pass
                except Exception:
                    continue
        
            symbol_url[missing_symbol] = url
    except:
        continue
    
def get_details(symbol):
    i = 1
    print(symbol)
    funda_analysis = {}
    for key in symbol:
        try:
         #print(key)
          
         l = []
         x = []
         if i % 50 == 0:
          #     driver.quit()
              os.system("taskkill /im chrome.exe /f")
         webbrowser.open_new(symbol[key])
         html_content =  requests.get(symbol[key])
         soup = BeautifulSoup(html_content.content, "html.parser")
         data = soup.find("div", attrs={"id": "stk_overview"})
        #print(type(data))
         for gdp_table_data in data.find_all("td"):
            for table in gdp_table_data:

                l.append(table)
         
         
         week_high = l[l.index('52 Week High')+1]
         if week_high.find(',') > 0:
             week_high = float(week_high.replace(',',''))
         else:
             week_high = float(week_high)
         week_low = l[l.index('52 Week Low')+1]
         if week_low.find(',') > 0:
             week_low = float(week_low.replace(',',''))
         else:
             
             week_low = float(week_low)
         
         high_low_ratio = week_high/week_low
         high_low_avg = (week_high+week_low)/2
         p_b = float(l[l.index("P/B")+1])
         div_yld = float(l[l.index('Dividend Yield')+1])
        #print(gdp_table_data)
         debt = soup.find("div", attrs={"id": "peers"})
         for get_debt in debt.find_all("td"):
             x.append(str(get_debt))
         for deb in x:
             if 'debtEquity' in deb:
                 debt = float(''.join(re.findall(r'\d+\.\d+',deb)))
                 break
        
         funda_analysis[key] = [high_low_ratio,high_low_avg,p_b,div_yld,debt]
         
         i = i + 1
        except:
            i = i + 1
            continue
        #if inc!= 1 and inc%29 == 1:
    
    return funda_analysis
xyz = get_details(symbol_url)
key_no_details = list(set(symbol_url.keys())-set(xyz.keys()))
dic_no_details = {key:val for key,val in symbol_url.items() if key in key_no_details}
return_2nd = get_details(dic_no_details)
funda_analysis = {**xyz,**return_2nd}
dff = pd.DataFrame.from_dict(funda_analysis, orient = 'index')
dff.columns = ['high_low_ratio','high_low_avg','p_b','div_yld','debt']
dff.to_excel(r'D:\Trade\Analysis\\' + output_name +'25112021.xlsx')