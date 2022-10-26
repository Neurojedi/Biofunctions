#!/usr/bin/env python
# coding: utf-8

# In[16]:


#The function below returns the list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times; you may return the elements in any order
def SpectrumConvolution(spectrum):
    spectrum=sorted(spectrum)
    convolution = []
    for i, cm in enumerate(spectrum[:-1]):
        for mass in spectrum[i+1:]:
            if mass == cm:
                continue
            convolution.append(mass - cm)
    convolution=sorted(convolution)
    return convolution
