# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:07:43 2024

@author: Karthick
"""

value = [1,2,3,4]
data = 0
try:
    data = value[3]
except IndexError:
    print('HR Indx')
except:
    print('Hacke')
finally:
    print('Finally')
    
data = 10
try:
    data = data /0
except ZeroDivisionError:
    print('HR')
finally:
    print('Finally')