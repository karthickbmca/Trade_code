# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:49:04 2021

@author: KarthickB
"""

import pandas as pd

y_day = '2021-05-06'

today = '2021-05-07'

dic_profit_shares = {}

df = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-07.xlsx')

df = df[(df['spinng_top']!=0) & (df['Date'] == today)]

df['diff'] = (df['High'] - df['Open'])/100*df['Open']

df.to_excel(r'C:\Users\KarthickB\Desktop\Trade\spn_top070521.xlsx')
