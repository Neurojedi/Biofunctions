#!/usr/bin/env python
# coding: utf-8

# In[16]:

from biofunctions.proteins.MassSpectrum import get_LinearSpectrum
def LinearPeptideScoring(spectrum, peptide):
    score = 1 
    linearspectrum = get_LinearSpectrum(peptide)
    order = 0
    for j in linearspectrum:
        i = order+1
        while i < len(spectrum):
            if spectrum[i] > j:
                break
            if spectrum[i] == j:
                score += 1
                order = i
                break
            i+=1     
    return score
