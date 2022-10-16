# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 01:05:12 2022

@author: User
"""
l = [['A','I','I'],['S','A','A'],['S','I','I']]
flat = set(sum(l,[]))
dic = {d:[0,0,0] for d in flat}
d_tot = {}

for x in l:
    for y in range(len(x)):
        c = 0
        w = 0
        lo = 0
        if y!=2:
            if dic[x[y]][0] == 0:
                dic[x[y]][0] = 1
            else:
                dic[x[y]][0] = dic[x[y]][0] + 1
        
       
        else:
            team = x[2]
            idx = x.index(team)
            if idx == 0:
                prev = 1
            else:
                prev = 0
            if dic[x[idx]][1] == 0:
                dic[x[idx]][1] = 1
            else:
                dic[x[idx]][1] = dic[x[idx]][1] + 1
                
            if dic[x[prev]][2] == 0:
                dic[x[prev]][2] = 1
            else:
                dic[x[prev]][2] = dic[x[prev]][2] + 1
                    
                
print(dic)