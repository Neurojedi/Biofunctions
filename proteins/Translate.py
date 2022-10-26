#!/usr/bin/env python
# coding: utf-8

# In[16]:


#The function below takes an RNA string Pattern and returns translation of Pattern into an amino acid string Peptide
from biofunctions.utils.Tables import codon_table
def get_translation(rna_string):
    result = ""
    len_string=len(rna_string)
    for i in range(0, len_string-2, 3):
        codon = rna_string[i: i+3]
        result += codon_table[codon]
    return result

