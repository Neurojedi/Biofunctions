#!/usr/bin/env python
# coding: utf-8

# In[109]:


# Given strings Sequence and Pattern as well as an integer d,
#we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches

from biofunctions.utils.hamming_distance import hamming_distance  

def countwithmismatches(sequence,pattern,d):
    count=0
    for i in range(len(sequence) - len(pattern)+1):
        if hamming_distance(pattern, sequence[i:i+len(pattern)]) <= d:
            count +=1 
    print(count)

