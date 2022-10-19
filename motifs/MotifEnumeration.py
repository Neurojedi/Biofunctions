#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches
# The function below returns these motifs by using a brute force algorithm.

from biofunctions.utils.pattern_control  import pattern_control
from biofunctions.utils.hamming_distance import hamming_distance
from biofunctions.utils.iterative_neighbors import iterative_neighbors
    
def MotifEnumeration(sequence, k, d):
    patterns = set()
    neighbor = set()
    item = sequence[0]
    len_item=len(item)
    for i in range(len_item-k+1):
        n = iterative_neighbors(item[i:i+k], d)
        neighbor = neighbor.union(n)
    for n in neighbor:
        existpattern = True
        for i in range(1, len(sequence)):
            if not pattern_control(n, sequence[i], d):
                existpattern = False
                break
        if existpattern:
            patterns.add(n)
    return print ('\n'.join(patterns))

