# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:18:17 2023

@author: User
"""
import pandas as pd
import pathlib
import re
import datetime
from datetime import timedelta

end = datetime.date.today()
#end = end - timedelta(days=1)
df = pd.read_excel(r'C:\Users\User\Downloads\emas, Technical Analysis Scanner (12).xlsx')[1:]

li = df['Unnamed: 2'].tolist()[::-1]
smart_shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in li})

pathlib.Path(r"E:\Trade\smart_list\smart_list_" + end.strftime('%d%m%Y') +".txt").write_text(smart_shares_top_prior)
