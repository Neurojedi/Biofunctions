#!/usr/bin/env python
# coding: utf-8

# In[15]:


# The function below utilizes FrequencyMap function and returns the most frequent K-mers.
from biofunctions.utils.frequency_map import frequency_map
def frequent_kmers(sequence, k):   

    frew_kmers = []   

    freq_map = frequency_map(sequence, k)   

    m = max(freq_map.values())   

    for most_frequent_kmer in freq_map:   

        if freq_map[most_frequent_kmer] == m:   
             frew_kmers.append(most_frequent_kmer)   

    return frew_kmers   


# In[ ]:




