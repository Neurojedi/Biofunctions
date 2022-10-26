#!/usr/bin/env python
# coding: utf-8

# In[16]:

from biofunctions.proteins.MassSpectrum import Cyclospectrum
def CyclopeptideScoring(spectrum, peptide_masses):
    score = 1 
    cyclospectrum = Cyclospectrum(peptide_masses)
    order = 0
    for j in cyclospectrum:
        i = order+1
        while i < len(spectrum):
            if spectrum[i] > j:
                break;
            if spectrum[i] == j:
                score += 1
                order = i
                break;
            i+=1      
    return score

