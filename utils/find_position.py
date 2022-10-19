#!/usr/bin/env python
# coding: utf-8

# In[18]:


# The functions below returns the starting positions where the specified pattern appears as a substring of Genome.
def find_position(sequence,pattern):
    starting_position=[]
    n=len(sequence)
    k=len(pattern)
    for i in range(n-k+1):
        if sequence[i:i+k]==pattern:
            starting_position.append(i)
    print(*starting_position)

