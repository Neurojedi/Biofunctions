#!/usr/bin/env python
# coding: utf-8

# In[41]:

from biofunctions.utils.hamming_distance import hamming_distance  
# Find all approximate occurrences of a pattern in a sequence with at most d mismatch
def approx_patternmatch(pattern, sequence, d):
    position = []
    lenseq=len(sequence)
    lenpat=len(pattern)
    for i in range (lenseq - lenpat+1):
        if hamming_distance(pattern, sequence[i:i + lenpat]) <= int(d):
            position.append(i)
    return print(*position)

