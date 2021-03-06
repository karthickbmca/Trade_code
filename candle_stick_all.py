# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 00:23:54 2021

@author: -
"""

import pandas as pd
import talib


data = pd.read_excel("C:\\Users\\KarthickB\\Desktop\\Trade\\data2021-04-30.xlsx")


data["cdl2crows"]=talib.CDL2CROWS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdl3blackcrows"]=talib.CDL3BLACKCROWS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdl3inside"]=talib.CDL3INSIDE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdl3linestrike"]=talib.CDL3LINESTRIKE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdl3outside"]=talib.CDL3OUTSIDE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdl3starsinsouth"]=talib.CDL3STARSINSOUTH(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdl3whitesoldiers"]=talib.CDL3WHITESOLDIERS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlabandonedbaby"]=talib.CDLABANDONEDBABY(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdladvanceblock"]=talib.CDLADVANCEBLOCK(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlbelthold"]=talib.CDLBELTHOLD(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlbreakaway"]=talib.CDLBREAKAWAY(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlclosingmarubozu"]=talib.CDLCLOSINGMARUBOZU(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlconcealbabyswall"]=talib.CDLCONCEALBABYSWALL(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlcounterattack"]=talib.CDLCOUNTERATTACK(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdldarkcloudcover"]=talib.CDLDARKCLOUDCOVER(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdldoji"]=talib.CDLDOJI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdldojistar"]=talib.CDLDOJISTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdldragonflydoji"]=talib.CDLDRAGONFLYDOJI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlengulfing"]=talib.CDLENGULFING(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdleveningdojistar"]=talib.CDLEVENINGDOJISTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdleveningstar"]=talib.CDLEVENINGSTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlgapsidesidewhite"]=talib.CDLGAPSIDESIDEWHITE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlgravestonedoji"]=talib.CDLGRAVESTONEDOJI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlhammer"]=talib.CDLHAMMER(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlhangingman"]=talib.CDLHANGINGMAN(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlharami"]=talib.CDLHARAMI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlharamicross"]=talib.CDLHARAMICROSS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlhighwave"]=talib.CDLHIGHWAVE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlhikkake"]=talib.CDLHIKKAKE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlhikkakemod"]=talib.CDLHIKKAKEMOD(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlhomingpigeon"]=talib.CDLHOMINGPIGEON(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlidentical3crows"]=talib.CDLIDENTICAL3CROWS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlinneck"]=talib.CDLINNECK(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlinvertedhammer"]=talib.CDLINVERTEDHAMMER(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlkicking"]=talib.CDLKICKING(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlkickingbylength"]=talib.CDLKICKINGBYLENGTH(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlladderbottom"]=talib.CDLLADDERBOTTOM(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdllongleggeddoji"]=talib.CDLLONGLEGGEDDOJI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdllongline"]=talib.CDLLONGLINE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlmarubozu"]=talib.CDLMARUBOZU(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlmatchinglow"]=talib.CDLMATCHINGLOW(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlmathold"]=talib.CDLMATHOLD(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlmorningdojistar"]=talib.CDLMORNINGDOJISTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlmorningstar"]=talib.CDLMORNINGSTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlonneck"]=talib.CDLONNECK(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlpiercing"]=talib.CDLPIERCING(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlrickshawman"]=talib.CDLRICKSHAWMAN(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlrisefall3methods"]=talib.CDLRISEFALL3METHODS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlseparatinglines"]=talib.CDLSEPARATINGLINES(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlshootingstar"]=talib.CDLSHOOTINGSTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlshortline"]=talib.CDLSHORTLINE(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlspinningtop"]=talib.CDLSPINNINGTOP(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlstalledpattern"]=talib.CDLSTALLEDPATTERN(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlsticksandwich"]=talib.CDLSTICKSANDWICH(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdltakuri"]=talib.CDLTAKURI(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdltasukigap"]=talib.CDLTASUKIGAP(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlthrusting"]=talib.CDLTHRUSTING(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdltristar"]=talib.CDLTRISTAR(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlunique3river"]=talib.CDLUNIQUE3RIVER(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlupsidegap2crows"]=talib.CDLUPSIDEGAP2CROWS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)
data["cdlxsidegap3methods"]=talib.CDLXSIDEGAP3METHODS(data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values)

data.to_excel("C:\\Users\\KarthickB\\Desktop\\Trade\\with_all_canstc_030521.xlsx")