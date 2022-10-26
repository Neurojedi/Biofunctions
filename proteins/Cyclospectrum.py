#!/usr/bin/env python
# coding: utf-8

# In[16]:


#The function below returns cyclospectrum of an peptide

from biofunctions.utils.Tables import amino_acid_masses
def Cyclospectrum(peptide):
    result = [0]
    masses = [amino_acid_masses[amino_acid] for amino_acid in peptide]
    acc = masses.copy()
    result.extend(acc)
    new_element = acc.copy()
    for j in range(len(peptide) - 2):
        for i in range(len(acc)):
            index = (i+j+1) % len(acc)
            new_element[i] += acc[index]
        result.extend(new_element)
    result.append(sum(acc))
    result=sorted(result)
    return result

