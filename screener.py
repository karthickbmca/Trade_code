# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:31:52 2022

@author: User
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

for missing_symbol in ['infy']:
    try:
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