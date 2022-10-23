#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns the k-universal circular string.
from biofunctions.assembly.EularianReconstruction import StringReconstruction

def GenerateKmers(k):
    kmers = []
    formatter = "{0:0>%db}" % k
    for i in range(2**k):
        kmers.append(formatter.format(i))
    return kmers

def get_CircularString(k):
    kmers = GenerateKmers(k)
    result = StringReconstruction(kmers)[:2**k]
    return result

