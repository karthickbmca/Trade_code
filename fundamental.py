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

file_name = 'profit_share_two_days27102021'
output_name = 'fundamental_analysis'
funda_analysis = {}
inc = 1
df = pd.read_excel(r'D:\\Trade\Analysis\\' + file_name+ '.xlsx')
url_link = pd.read_excel(r'D:\Trade\Analysis\money_control_url.xlsx')
url_symbol = url_link['SYMBOL'].tolist()
url_full = url_link['url'].tolist()
driver = webdriver.Chrome(executable_path=r'C:\Users\Karthik\Downloads/chromedriver.exe')
for symbol in df['Symbol'].tolist():
    try:
        if (inc == 1) or (inc % 10 == 0):
            if inc != 1:
                driver.close()
            driver = webdriver.Chrome(executable_path=r'C:\Users\Karthik\Downloads/chromedriver.exe')
        
        if symbol not in url_symbol:
            driver.get('https://www.google.com/search?q='+symbol+'+share+price')
            content = driver.find_elements_by_tag_name("a")
            for rs in content:
                try:
                    if type(rs.get_attribute('href')) == str:
                        if 'moneycontrol' in rs.get_attribute('href'):
                           url = rs.get_attribute('href')
                        else:
                            pass
                except Exception as E:
                    continue
        else:
            url = url_full[url_symbol.index(symbol)]
        # Make requests from webpage
        l = []
        x = []
        
        driver.get(url)
       #time.sleep(5)
        html_content = requests.get(url)
        soup = BeautifulSoup(html_content.content, "html.parser")
        data = soup.find("div", attrs={"id": "stk_overview"})
       #print(type(data))
        for gdp_table_data in data.find_all("td"):
           for table in gdp_table_data:
               l.append(table)
        week_high = float(l[l.index('52 Week High')+1])
        week_low = float(l[l.index('52 Week Low')+1])
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
       
        funda_analysis[symbol] = [high_low_ratio,high_low_avg,p_b,div_yld,debt]
       #if inc!= 1 and inc%29 == 1:
       #print(funda_analysis)
       
   

    


    except:
# driver.close()
# driver = webdriver.Chrome(executable_path=r'C:\Users\Karthik\Downloads/chromedriver.exe')
        continue
    
    inc = inc + 1           
dff = pd.DataFrame.from_dict(funda_analysis, orient = 'index')
dff.columns = ['high_low_ratio','high_low_avg','p_b','div_yld','debt']
dff.to_excel(r'D:\Trade\Analysis\\' + output_name +'271021.xlsx')