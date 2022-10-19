#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Skew is the difference between the total number of occurrences of G and the total number of occurrences of C in the first i nucleotides of Genome.
# The function below finds the positions in a genome where the skew diagram attains a minimum.
# 
def get_skew(seq):
    skew = 0
    skew_list= []
    skew_list.append(0)
    n=len(seq)
    for i in range(n):
        if seq[i] == 'C' :
            skew = skew - 1
        elif seq[i] == 'G':
            skew += 1
        else:
            skew = skew
        skew_list.append(skew)
    return skew_list

 

def min_skew(sequence):
    skew_list = get_skew(sequence)
    min_skew = min(skew_list)
    min_skew_list = list()
    
    n=len(sequence)
    for i in range(n):
        if skew_list[i] == min_skew:
            min_skew_list.append(i)
    print(*min_skew_list, sep='\n')

