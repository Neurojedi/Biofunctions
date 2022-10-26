#!/usr/bin/env python
# coding: utf-8

# In[16]:


#The function below returns the score of Peptide against Spectrum.

from biofunctions.utils.Tables import amino_acid_masses as amino_acid_masses
from biofunctions.proteins.Cyclospectrum import Cyclospectrum
def PeptideScore(peptide,spectrum):
    peptide_score = Cyclospectrum(peptide)
    score = 0
    for m in set(spectrum):
        score += min(peptide_score.count(m),spectrum.count(m))
    return score

