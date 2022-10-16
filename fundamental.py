# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:05:09 2021

@author: Karthik
"""
from selenium import webdriver
import pandas as pd
import re
import sched, time
from bs4 import BeautifulSoup
import requests
from IPython.core.display import HTML

#driver1 = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

file_name = 'profit_share_two_days25112021'
output_name = 'fundamental_analysis'
funda_analysis = {}
inc = 1
driver = webdriver.Chrome(executable_path=r'C:\Users\User\Downloads/chromedriver.exe')
driver.get('https://www.screener.in/company/APEX/')
url = 'https://www.screener.in/company/APEX/'
html_content = requests.get(url)
soup = BeautifulSoup(html_content.content, "html.parser")
data = soup.find("div", attrs={"id": "stk_overview"})
#print(type(data))
l= []
x=[]
for gdp_table_data in data.find_all("td"):
   for table in gdp_table_data:
       l.append(table)
       
debt = soup.find("div", attrs={"id": "peers"})
for get_debt in debt.find_all("td"):
   x.append(str(get_debt))
for deb in x:
   if 'debtEquity' in deb:
       debt = float(''.join(re.findall(r'\d+\.\d+',deb)))
       break
