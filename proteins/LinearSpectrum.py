#!/usr/bin/env python
# coding: utf-8

# In[16]:
from biofunctions.utils.Tables import amino_acid_masses
def get_LinearSpectrum(peptide):
    len_pep=len(peptide)
    mass = [0] * (len_pep + 1)
    for i, aa in enumerate(peptide):
        mass[i+1] = mass[i] + amino_acid_masses[aa]
    
    linear_spectrum = [0]
    len_mass=len(mass)
    for i in range(len_mass):
        for j in range(i+1, len(mass)):
            linear_spectrum.append(mass[j] - mass[i])
    linear_spectrum=sorted(linear_spectrum)
    return linear_spectrum

