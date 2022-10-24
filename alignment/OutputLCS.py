#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given two strings s and t, the function below returns a longest common subsequence of s and t
def BackTracker(v, b):
    lv = len(v)
    lb = len(b)
    sub = [[0] * (lb+1) for i in range(lv+1)] 
    bt = [[0] * (lb+1) for i in range(lv+1)] 
    sub[0][0] = 0
    bt[0][0] = 0
    for i in range(1, lb):
        sub[0][i] = 0
        bt[0][i] = b[i-1]
    for i in range(1, lv):
        sub[i][0] = 0
        bt[i][0] = v[i-1]
    for i in range(1, lv+1):
        for j in range(1, lb+1):
            match = 0
            if v[i-1] == b[j-1]:
                match = 1
            sub[i][j] = max(
                sub[i][j-1], sub[i-1][j], sub[i-1][j-1] + match,
            )
            if sub[i][j] == sub[i-1][j]:
                bt[i][j] = "|"
            elif sub[i][j] == sub[i][j-1]:
                bt[i][j] = "-"
            elif sub[i][j] == sub[i-1][j-1]+match:
                bt[i][j] = "+"
    return bt

def OutputLCS(backtrack, k, l, m): # k l m
    result = ""
    while l > 0 and m > 0:
        if l == 0 or m == 0:
            return ""
        if backtrack[l][m] == "|":
            l -= 1
        elif backtrack[l][m] == "-":
            m -= 1
        else:
            result = k[l-1] + result
            m -= 1
            l -= 1
    return result

