#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below reconstructs a string from its genome path. 
#Input A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbolsof Patterni+1 for 1 ≤ i ≤ n-1.
#Output is A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).
def PathToGenome(genome_list):
    path=''
    genome_list=genome_list.split(' ')
    for i in genome_list[:-1]:
        path+=i[0]
    path = path +genome_list[-1]
    return path

