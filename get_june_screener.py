# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:12:51 2022

@author: User
"""
import urllib.request
 
# pretty-print python data structures
from pprint import pprint
from nsetools import Nse
from nsepy import get_history
from html_table_parser.parser import HTMLTableParser

 
import pandas as pd
import time

def url_get_contents(url):
 
    # Opens a website and read its
    # binary contents (HTTP Response Body)
 
    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
 
    #reading contents of the website
    return f.read()
 
# defining the html contents of a URL.

def comma(val):
    if ',' in val:    
        return val.replace(',','')
    else:
        return val
    
nse = Nse()
d = {}
nse = Nse()
#q = nse.get_quote('infy')
all_stock_codes = nse.get_stock_codes() 
#all_stock_codes = pd.read_csv(r'E:\Trade\profit_list\profit_stocks08072022.txt')
#all_stock_codes = ['3IINFOLTD']
for stock in all_stock_codes:
    print(stock)
    if stock[:1] == 'N':
        try:
            try:
                xhtml = url_get_contents('https://www.screener.in/company/'+ stock + '/consolidated').decode('utf-8')
                p = HTMLTableParser()
                p.feed(xhtml)
                p.tables[0][1][-2]
               
            except:
                time.sleep(1)
                xhtml = url_get_contents('https://www.screener.in/company/'+ stock + '/').decode('utf-8')
                p = HTMLTableParser()
                 
                # feeding the html contents in the
                # HTMLTableParser object
                p.feed(xhtml)
        # Defining the HTMLTableParser object
            if p.tables[0][0][-1] == 'Jun 2022':
                l= []
                for idx1 in range(0,len(p.tables)):
                    for idx2 in range(0,len(p.tables[idx1])):
                        if idx1 == 0:
                            if p.tables[idx1][idx2][0] == 'Sales +':
                                p_qtr = float(comma(p.tables[idx1][idx2][-2]))
                                c_qtr = float(comma(p.tables[idx1][idx2][-1]))
                                try:
                                    qtr_sal = (c_qtr - p_qtr)/p_qtr *100
                                except:
                                    qtr_sal = 'Divide 0'
                                l.append(p_qtr)
                                l.append(c_qtr)
                                l.append(qtr_sal)
                                
                            if p.tables[idx1][idx2][0] == 'Operating Profit':
                                p_opr_prf = float(comma(p.tables[idx1][idx2][-2]))
                                c_opr_prf= float(comma(p.tables[idx1][idx2][-1]))
                                try:
                                    qtr_opr_prf = (c_opr_prf - p_opr_prf)/p_opr_prf *100
                                except:
                                    qtr_opr_prf = 'Divide 0'
                                l.append(p_opr_prf)
                                l.append(c_opr_prf)
                                l.append(qtr_opr_prf)
                                
                            if p.tables[idx1][idx2][0] == 'Net Profit':
                                p_net_prf = float(comma(p.tables[idx1][idx2][-2]))
                                c_net_prf= float(comma(p.tables[idx1][idx2][-1]))
                                try:
                                    qtr_net_prf = (c_net_prf - p_net_prf)/p_net_prf *100
                                except:
                                    qtr_net_prf = 'Divide 0'
                                l.append(p_net_prf)
                                l.append(c_net_prf)
                                l.append(qtr_net_prf)
                            if p.tables[idx1][idx2][0] == 'Other Income +':
                                other_income = float(comma(p.tables[idx1][idx2][-1]))
                                l.append(other_income)
                                    
                d[stock] = l
        except:
            time.sleep(1)
            continue

df_screener = pd.DataFrame.from_dict(d, orient = 'index')
df_screener.columns = ['prev_qtr_sales','curr_qtr_sales','perc_imp_sales','prev_qtr_oprPro','curr_qtr_oprPro','perc_imp_oprPro','prev_qtr_NetPro','other_income','curr_qtr_NetPro','perc_imp_NetPro']
df_screener.to_excel("E:\Trade\Analysis\\screener_data_june_8Aug_1.xlsx")
        
    
    