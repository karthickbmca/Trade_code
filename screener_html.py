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
#all_stock_codes = nse.get_stock_codes() 
#all_stock_codes = pd.read_csv(r'E:\Trade\profit_list\profit_stocks08072022.txt')
all_stock_codes = ['infy']
for stock in all_stock_codes:
    print(stock)
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
                    
        
                if idx1 == 1:
                    
                     if p.tables[idx1][0][-1] != 'TTM':
                         if p.tables[idx1][idx2][0] == 'Sales +':
                             p_anl = float(comma(p.tables[idx1][idx2][-2]))
                             c_anl = float(comma(p.tables[idx1][idx2][-1]))
                             try:
                                 anl_sal = (c_anl - p_anl)/p_anl *100
                             except:
                                 anl_sal = 'Divide 0'
                             l.append(p_anl)        
                             l.append(c_anl)
                             l.append(anl_sal)
                         if p.tables[idx1][idx2][0] == 'Operating Profit':
                             p_opr_prf_a = float(comma(p.tables[idx1][idx2][-2]))
                             c_opr_prf_a= float(comma(p.tables[idx1][idx2][-1]))
                             try:
                                 opr_prf_a = (c_opr_prf_a - p_opr_prf_a)/p_opr_prf_a * 100
                             except:
                                 opr_prf_a = 'Divide 0'
                             l.append(p_opr_prf_a)
                             l.append(c_opr_prf_a)
                             l.append(opr_prf_a) 
                         if p.tables[idx1][idx2][0] == 'Net Profit':
                             p_net_prf_a = float(comma(p.tables[idx1][idx2][-2]))
                             c_net_prf_a= float(comma(p.tables[idx1][idx2][-1]))
                             try:
                                 net_prf_a = (c_net_prf_a - p_net_prf_a)/p_net_prf_a * 100
                             except:
                                 net_prf_a = 'Divide 0'
                             l.append(p_net_prf_a)
                             l.append(c_net_prf_a)
                             l.append(net_prf_a)         
                        
                     else:
                         if p.tables[idx1][idx2][0] == 'Sales +':
                             p_anl = float(comma(p.tables[idx1][idx2][-2]))
                             c_anl = sum([float(comma(x)) for x in p.tables[idx1-1][idx2][-3:]]) + float(comma(p.tables[idx1][idx2][-1]))
                             try:
                                 anl_sal = (c_anl - p_anl)/p_anl *100
                             except:
                                 anl_sal = 'Divide 0'
                             l.append(p_anl)        
                             l.append(c_anl)
                             l.append(anl_sal)
                             
                         if p.tables[idx1][idx2][0] == 'Operating Profit':
                             p_opr_prf_a = float(comma(p.tables[idx1][idx2][-2]))
                             c_opr_prf_a= sum([float(comma(x)) for x in p.tables[idx1-1][idx2][-3:]] )+ float(comma(p.tables[idx1][idx2][-1]))
                             try:
                                 opr_prf_a = (c_opr_prf_a - p_opr_prf_a)/p_opr_prf_a * 100
                             except:
                                 opr_prf_a = 'Divide 0'
                             l.append(p_opr_prf_a)
                             l.append(c_opr_prf_a)
                             l.append(opr_prf_a) 
                             
                         if p.tables[idx1][idx2][0] == 'Net Profit':
                             p_net_prf_a = float(comma(p.tables[idx1][idx2][-2]))
                             c_net_prf_a = sum([float(comma(x)) for x in p.tables[idx1-1][idx2][-3:]]) + float(comma(p.tables[idx1][idx2][-1]))
                             try:
                                 net_prf_a = (c_net_prf_a - p_net_prf_a)/p_net_prf_a * 100
                             except:
                                 net_prf_a = 'Divide 0'
                             l.append(p_net_prf_a)
                             l.append(c_net_prf_a)
                             l.append(net_prf_a)         
                                
                if p.tables[idx1][idx2][0] == 'Public +':
                    public_holders = p.tables[idx1][idx2][-1]
                    l.append(public_holders)
                    
        d[stock] = l
         
    except:
        time.sleep(1)
        continue
    
df_screener = pd.DataFrame.from_dict(d, orient = 'index')
df_screener.columns = ['prev_qtr_sales','curr_qtr_sales','perc_imp_sales','prev_qtr_oprPro','curr_qtr_oprPro','perc_imp_oprPro','prev_qtr_NetPro','curr_qtr_NetPro','perc_imp_NetPro','prev_anl_sales','curr_anl_sales','perc_imp_sales_anl','prev_anl_oprPro','curr_anl_oprPro','perc_imp_oprPro_anl','prev_anl_NetPro','curr_anl_NetPro','perc_imp_NetPro_anl','public_holding']
df_screener.to_excel("E:\Trade\Analysis\\screener_data_all.xlsx")

        
            
            