#!/usr/bin/env python
# coding: utf-8

# In[16]:

#The function below returns the number of linear peptides having integer mass m
from biofunctions.utils.Tables import mass_list
def CountingMass(Mass,mlist):
    if Mass == 0: return 1, mlist
    if Mass < 57: return 0, mlist
    if Mass in mlist: return mlist[Mass], mlist
    n = 0
    for i in mass_list:
        k, mlist = CountingMass(Mass - i, mlist)
        n += k
    mlist[Mass] = n
    return n, mlist