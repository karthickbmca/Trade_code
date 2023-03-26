# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:43:45 2023

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
    
d={}
xhtml = url_get_contents('https://www.moneycontrol.com/markets/earnings/results-calendar/?classic=true').decode('utf-8')
p = HTMLTableParser()
p.feed(xhtml)
l=p.tables
for x in range(len(l[1])):
    #print (l[1][x])
    d[l[1][x][0]] = l[1][x][1:]
df_screener = pd.DataFrame.from_dict(d, orient = 'index')    
df_screener.columns = ['Date','Live Price','Change','52W High','52W Low']
df_screener.to_excel("E:\Trade\Analysis\\dates.xlsx")
