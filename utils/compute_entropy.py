#!/usr/bin/env python
# coding: utf-8

# In[21]:


# The function below computes entropy for a given profile matrix.
from biofunctions.get_profile import get_profile
def compute_entropy(motifs):
    profile_matrix = get_profile(motifs)
    ent = {}
    columns = len(motifs[0])
    for char in CHARS:
        for i in range(columns):
            x = profile_matrix[char][i]
            if x:
                if x in ent:
                    ent[x] += 1
                else:
                    ent[x] = 1

    entropy = 0
    for x in ent:        
        entropy +=  ent[x] * x * math.log2(x)
    
    return entropy

