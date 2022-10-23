#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

# The function below returns  a string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string exists)

def StringSpelledByGappedPatterns(pattern_list, d):
    
    GappedPatterns = []
    GappedPatterns.append(pattern_list.split('|'))
    len_pattern = len(GappedPatterns[0][0])
    Prefix = ''
    Suffix= ''
    for i, pair in enumerate(GappedPatterns):
        if i != len(GappedPatterns) - 1:
            Prefix += pair[0][0]
            Suffix += pair[1][0]
        else:
            Prefix += pair[0]
            Suffix += pair[1]
    return Prefix + Suffix[len(Suffix) - len_pattern - d: ]
