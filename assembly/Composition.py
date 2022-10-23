#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns Compositionk(Text), where the k-mers are arranged in lexicographic order.
def composition(seq, k, sort=True):
    kmers = list()
    len_seq=len(seq)
    for i in range(len_seq-k+1):
        kmers.append(seq[i:i+k])
    if sort:
        sorted_kmers=sorted(kmers)
        return sorted_kmers
    return kmers

