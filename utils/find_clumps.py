#!/usr/bin/env python
# coding: utf-8

# In[38]:


# The function below finds the all distinct k-mers that forms a clump (the k-mer and its reverse complement).
from biofunctions.utils.frequency_map import frequency_map
def find_clumps(sequence, k, L, t):
    patterns = []
    n = len(sequence)
    for value in range(n - L):
        window = sequence[value:value+L]
        frequqncy_Map = frequency_map(window, k)
        for key in frequqncy_Map:
            if frequqncy_Map[key] >= t:
                patterns.append(key)
    return list(dict.fromkeys(patterns))

