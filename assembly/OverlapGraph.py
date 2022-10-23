#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns the overlap graph Overlap(Patterns), in the form of an adjacency list. 
from itertools import combinations
def overlap_graph(pattern_list):
    adjacency_list = list()
    for (i, kmer1), (j, kmer2) in combinations(enumerate(pattern_list), 2):
        if kmer1[1:] == kmer2[:-1]:
            adjacency_list.append((i, j))
        if kmer2[1:] == kmer1[:-1]:
            adjacency_list.append((j, i))
    return adjacency_list

def get_graph(pattern_list, adjacency_list,printer=False):
    edges = [
        f'{pattern_list[i]} -> {pattern_list[j]}' # For Bioinformatics Course, you should use : instead of ->
        for i, j in adjacency_list
    ]
    kmer_list='\n'.join(edges).split('\n')
    kmer_list=sorted(kmer_list)
    if printer==False:
        return kmer_list
    else:
        return print('\n'.join(kmer_list))

