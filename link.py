# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:21:24 2021

@author: Karthik
"""

from selenium import webdriver
from nsetools import Nse
import pandas as pd
import re
import sched, time
from bs4 import BeautifulSoup
import requests
from IPython.core.display import HTML
nse = Nse()
#q = nse.get_quote('infy')
all_stock_codes = nse.get_stock_codes() 


#driver1 = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


url = {}
inc = 1
df = pd.read_excel(r'D:\Trade\Analysis\money_control_url.xlsx')
driver = webdriver.Chrome(executable_path=r'C:\Users\Karthik\Downloads/chromedriver.exe')
for symbol in df['SYMBOL'].tolist():
    try:
        if 'google' in str(df[df['SYMBOL'] == symbol]['url']).split()[1]:
            if (inc == 1) or (inc % 10 == 0):
                if inc != 1:
                    driver.close()
                driver = webdriver.Chrome(executable_path=r'C:\Users\Karthik\Downloads/chromedriver.exe')
            driver.get('https://www.google.com/search?q='+symbol+'+share+price')
            
            content = driver.find_elements_by_tag_name("a")
            for rs in content:
                try:
                    if type(rs.get_attribute('href')) == str:
                        if 'www.moneycontrol' in rs.get_attribute('href'):
                           url_link = rs.get_attribute('href')
                           url[symbol] = url_link
                           
                except:
                    continue
    except:
        continue
    inc = inc + 1