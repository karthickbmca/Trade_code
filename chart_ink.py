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
#end = end - timedelta(days=3)
df = pd.read_excel(r'C:\Users\User\Downloads\emas_1, Technical Analysis Scanner (23).xlsx')[1:]
li = df['Unnamed: 2'].tolist()[::-1]
mfs = ['PSUBANKICI','IDFNIFTYET','HDFCVALUE','ICICIBANKP','ICICIQTY30','NPBET','SETFNN50','KOTAKBKETF','BANKBEES','SBIETFQLTY','MOVALUE','ICICIFIN','HDFCNIFBAN','NIFTYQLITY','SBIETFPB','DSPITETF','LOWVOL','NEXT50','SETFNIFBK','NIF100BEES','NV20BEES','ICICICOMMO','AXSENSEX','ICICIBANKN','BFSI','ABSLBANETF','ICICIALPLV','MOM50','TNIDETF','SETFNIF50','ICICIMOM30','INFRABEES','ICICINXT50','BSLNIFTY','DSPN50ETF','AXISNIFTY','HDFCLOWVOL','JUNIORBEES','SBIETFIT','KOTAKCONS','UTISENSETF','AUTOBEES','MOMOMENTUM','AXISTECETF','MAKEINDIA','MOLOWVOL','KOTAKLOVOL','ICICINIFTY','ABSLNN50ET','HDFCNIFTY','KOTAKNIFTY','UTINEXT50','NIFTYBEES','LICNETFSEN','ICICINV20','HDFCNIF100','HDFCSENSEX','ESG','IBMFNIFTY','UTISXN50','KOTAKALPHA','DBSTOCKBRO','DSPNEWETF','SETF10GILT','ICICINF100','LTGILTBEES','LICNETFGSC','ICICILOVOL','ICICITECH','DIVOPPBEES','TECH','ITBEES','AXISCETF','LICNETFN50','KOTAKNV20','SHARIABEES','ICICISENSX','ICICIAUTO','GILT5YBEES','ICICI5GSEC','MOGSEC','BSLSENETFG','KOTAKIT','HDFCGROWTH','CONSUMBEES','NETF','ICICICONSU','SDL24BEES','LIQUID','SDL26BEES','AXISBPSETF','HEALTHY','ICICIPHARM','AXISHCETF','ICICI500','GSEC10YEAR','ICICIFMCG','PHARMABEES','MAHKTECH','AXISILVER','DSPPSBKETF','MOHEALTH','MON100','DSPSILVETF','KOTAKSILVE','MAFANG','MASPTOP50','ICICISILVE','HDFCSILVER','SBIETFCON','DSPBANKETF','SILVERBEES','SILVER','SILVRETF','GOLDETF','HDFCPVTBAN','ICICI10GS','LIQUIDBEES','NIFTYETF','MOQUALITY','KOTAKMNC','HDFCNEXT50','NIFMID150','HDFCMOMENT','MID150BEES','MOM100','KOTAKMID50','ICICIM150','HDFCMID150','CPSEETF','UTINIFTETF','ICICIMCAP','NAM_INDIA','DSPQ50ETF','HDFCSML250','NIFTY50PR1XINV','ABSLAMC']
smart_shares_top_prior = ','.join({'NSE:'+re.sub('[&-]','_',key)for key in li if key not in mfs})

pathlib.Path(r"E:\Trade\smart_list\smart_list_" + end.strftime('%d%m%Y') +".txt").write_text(smart_shares_top_prior)

sample_data = pd.read_csv('E:\Trade\Analysis\Equity.csv')
data_eq = sample_data[['Security Id','Igroup Name','ISubgroup Name']]
data_eq['Security Id'] = data_eq['Security Id'].astype(str)
#df_profit.to_excel(r'E:\Trade\Analysis\profit_share_' + end.strftime('%d%m%Y') +'.xlsx')
#get_profit_data = pd.read_excel(r'E:\Trade\Analysis\profit_share_' + end.strftime('%d%m%Y') +'.xlsx')
#get_profit_data.columns = ['Security Id','perc','yes_clos','tod_close','result','Morn_star','Bull_eng']
#df_get_less_percent = get_profit_data[(get_profit_data['perc'] >=0) & (get_profit_data['perc'] <=1) & (get_profit_data['tod_close'] <=1000)]
#list_less_one = df_get_less_percent['Security Id'].tolist()
#get_profit_data['Security Id'] = get_profit_data['Security Id'].astype(str)
get_sector = df.merge(data_eq,left_on=(['Unnamed: 2']),right_on=(['Security Id']),how='left')[['Security Id','Igroup Name']]
print(get_sector.groupby(['Igroup Name']).count().sort_values(by = ['Security Id'], ascending=False))

