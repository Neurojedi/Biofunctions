#!/usr/bin/env python
# coding: utf-8

# In[16]:


#The function below returns the number of subpeptides of a linear peptide of length n

def LinearSubpeptideCount(x):
    count = 0
    for i in range(1, x + 1):
        if i <= 2:
            count+= 2
        else:
            count+=i
    return count

