# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 01:05:15 2022

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


try:
    
    xhtml = url_get_contents('https://www.moneycontrol.com/markets/earnings/results-calendar/').decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    x = p.tables
    
    
        
except:
    pass