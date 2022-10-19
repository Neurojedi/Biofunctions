#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Given a motif find the profile matrix

import numpy as np
import math

CHARS = "ACGT"

def get_profile(motifs):    
    counts = {}
    profiles = {}
    columns = len(motifs[0])
    rows = len(motifs)
    
    for c in CHARS:
        counts[c] = np.zeros(columns)
        profiles[c] =  list(np.zeros(columns))

    for i in range(columns):
        for j in range(rows):
            counts[motifs[j][i]][i] += 1
    
    for i in range(columns):
        s = counts[CHARS[0]][i] + counts[CHARS[1]][i] + counts[CHARS[2]][i] + counts[CHARS[3]][i]
        for x in CHARS:
            profiles[x][i] = counts[x][i] / s
        
    return profiles


# In[ ]:




