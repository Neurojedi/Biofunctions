#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Given a Sequence generate d-neighborhood Neighbors(Pattern, d), the set of all k-mers whose Hamming distance from Pattern does not exceed d

chars = "ACGT"

def recursive_neighbors(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return [pattern] # base case

    neighbors_reduced = recursive_neighbors(pattern[1:], d-1)
    new_arr= [c + n for n in neighbors_reduced for c in chars if c != pattern[0]]

    if (d < len(pattern)):
        neighbors_reduced = recursive_neighbors(pattern[1:], d)
        new_arr += [pattern[0] + n for n in neighbors_reduced]

    return new_arr

