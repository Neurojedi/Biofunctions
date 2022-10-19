#!/usr/bin/env python
# coding: utf-8

# In[18]:


# The function finds the complementary sequence of a given sequence.
base_map = {'A':'T','T':'A','C':'G','G':'C'}
def complementary(sequence):
    comp = ''
    n = len(sequence)
    for i in range(n):
        comp += base_map[sequence[n - i - 1]]
    return comp

