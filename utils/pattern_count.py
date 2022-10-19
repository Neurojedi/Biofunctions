#!/usr/bin/env python
# coding: utf-8

# In[4]:


# The function below finds the number of occurance of a pattern in a sequence.
def pattern_count(pattern,  sequence):
    count_pattern=0
    for i in range(0, len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)]==pattern:
            count_pattern += 1
    return count_pattern

