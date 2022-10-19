#!/usr/bin/env python
# coding: utf-8

# In[27]:


# The function below calculates the hamming distance between two sequence.
def hamming_distance(sequence1,sequence2):
    hamming_score=0
    n1=len(sequence1)# n1 must be equal to len(sequence2)
    for i in range(n1):
        if sequence1[i] != sequence2[i]:
            hamming_score+=1
    return hamming_score

