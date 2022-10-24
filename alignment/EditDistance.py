#!/usr/bin/env python
# coding: utf-8

# In[1]:

# The function below returns the edit distance between two strings
def EditDistance(seq1, seq2):
    ls1 = len(seq1)
    ls2 = len(seq2)
    S = [[0] * (ls2+1) for i in range(ls1+1)]
    for i in range(1, ls1+1):
        S[i][0] = i
    for j in range(1, ls2+1):
        S[0][j] = j

    for i in range(1, ls1+1):
        for j in range(1, ls2+1):
            str_seq1 = seq1[i-1]
            str_seq2 = seq2[j-1]
            match = 1
            if str_seq1 == str_seq2:
                match = 0
            S[i][j] = min(
                S[i-1][j] + 1,
                S[i][j-1] + 1,
                S[i-1][j-1] + match
            )
    return S[-1][-1]


