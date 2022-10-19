#!/usr/bin/env python
# coding: utf-8

# In[13]:


# The function below returns the number of occurance for spesific patterns. 
# For instance, pass your sequence and k=1 to see how many times each nucleotide occur in the sequence you have.

def frequency_map(sequence, k):   

    frequency_list = {}   
    count = len(sequence)   
    
    for i in range(count-k+1):   
        pattern = sequence[i : i + k]   
        if pattern in frequency_list:   
            frequency_list[pattern] += 1   
        else:   
            frequency_list[pattern] = 1   
            
    return frequency_list   


# In[ ]:




