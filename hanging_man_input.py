# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:18:00 2021

@author: KarthickB
"""


import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpdates
import openpyxl
from datetime import datetime
import openpyxl
  
#plt.style.use('dark_background')

global_num = pd.DataFrame()

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-27onemonth.xlsx')

dic_buy = {}
next_day = datetime(2021,4,26)

filter_date = datetime(2021,5,26)

list_stocks = list(data[(data['hammer'] != 0) & (data['Date'] == filter_date)]['Symbol'])

axis = 2
writer = pd.ExcelWriter(r'C:\Users\KarthickB\Desktop\Trade\input_hammer2705.xlsx', engine = 'xlsxwriter')
global_num.to_excel(writer, sheet_name='Sheet1')

for syb in list_stocks:

        data = pd.read_excel(r'C:\Users\KarthickB\Desktop\Trade\data2021-05-27onemonth.xlsx')
        data = data[data['Symbol'] == syb]
        data = data[['Date', 'Open', 'High', 
                 'Low', 'Close']]
          
        # convert into datetime object
        data['Date'] = pd.to_datetime(data['Date'])
          
        # apply map function
        data['Date'] = data['Date'].map(mpdates.date2num)
          
        # creating Subplots
        fig, ax = plt.subplots()
          
        # plotting the data
        candlestick_ohlc(ax, data.values, width = 0.6,
                         colorup = 'green', colordown = 'red', 
                         alpha = 0.8)
          
        # allow grid
        #ax.grid(True)
          
        # Setting labels 
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
          
        # setting title
        plt.title(syb)
          
        # Formatting Date
        date_format = mpdates.DateFormatter('%d-%m-%Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()
          
        fig.tight_layout()
        
        plt.savefig(syb + ".png")  
        # show the plot
        plt.show()
        
        img = openpyxl.drawing.image.Image(syb + ".png")
        img.anchor = 'A' + str(axis)
        syb = ws.cell(row = (axis-1),column=1)
        ws.add_image(img)
        
        wb.save(r'C:\Users\KarthickB\Desktop\Trade\input_hammer2705.xlsx')
        axis = axis + 20



