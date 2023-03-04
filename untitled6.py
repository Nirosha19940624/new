# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:05:48 2023

@author: Administrator
"""

import numpy as np
import pandas as pd



#Read csv files
df_aus = pd.read_csv("C:/Users/Administrator/Desktop/New folder (2)/Australia_agriculture.csv")
print(df_aus.head())
df_uk = pd.read_csv("C:/Users/Administrator/Desktop/New folder (2)/United Kingdon_agriculture.csv")
print(df_uk.head())
df_china = pd.read_csv("C:/Users/Administrator/Desktop/New folder (2)/China_agriculture.csv")

a = np.array([[1,2],[-3,4]])
print(np.count_nonzero(a < 1))


b = np.array([1,2,3,4])
c = np.sqrt(b)
print(c)

e = np.array([1,2,3,4])
f = np.array([1,2,3,4,5,6,7,8,9,10])
mean = np.average(10)

stand = np.sqrt(np.mean((e - np.mean(e)) **2 ))
print(stand)


lll = np.prod(e[e % 2 ==1] **2)
print(lll)            

yy = np.sum(f[np.abs(f - np.mean(f)) > np.std(f)])
print(yy)


g = np.array([[1,2],[-3,4]])
z = np.sum(g > np.mean(g,axis=None),axis=0)
print(z)

g = np.array([[1,2],[-3,4]])
z = np.sum(g < np.mean(g,axis=1),axis=0)
print(z)




