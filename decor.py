# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 00:06:45 2023

@author: User
"""


    
    
def outer(myfunction):
    def inner():
        data = myfunction()
        return data.upper()
    return inner()



@outer
def myfunction():
    
    return 'Hello Worlds'

print(myfunction)