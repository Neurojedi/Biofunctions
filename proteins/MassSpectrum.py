#!/usr/bin/env python
# coding: utf-8

# In[16]:


from biofunctions.utils.Tables import amino_acid_masses
def Cyclospectrum(masses):
    result = [0]
    masses = [int(mass) for mass in masses]
    acc = masses.copy()
    result.extend(acc)
    new_element = acc.copy()
    for j in range(len(masses) - 2):
        for i in range(len(acc)):
            index = (i+j+1) % len(acc)
            new_element[i] += acc[index]
        result.extend(new_element)
    result.append(sum(acc))
    result=sorted(result)
    return result

def get_LinearSpectrum(peptide_mass):
    len_pep=len(peptide_mass)
    mass = [0] * (len_pep + 1)
    for i, aa in enumerate(peptide_mass):
        mass[i+1] = mass[i] + int(aa)
    
    linear_spectrum = [0]
    len_mass=len(mass)
    for i in range(len_mass):
        for j in range(i+1, len(mass)):
            linear_spectrum.append(mass[j] - mass[i])
    linear_spectrum=sorted(linear_spectrum)
    return linear_spectrum

