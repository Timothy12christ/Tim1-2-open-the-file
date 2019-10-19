# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:25:57 2019

@author: ASUS
"""

o=[]
with open ('C:/Users/ASUS/Desktop/food.txt','r') as f:
    for s in f:
        o.append(s.strip())
print(o)
