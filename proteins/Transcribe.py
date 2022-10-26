#!/usr/bin/env python
# coding: utf-8

# In[16]:

from biofunctions.utils.Tables import nucleotide_map,reverse_nucleotide_map
def get_transcription(string, reverse=False):
    result = ""
    if not reverse:
        return string.replace("T", "U")
    for base in string[::-1]:
        result += nucleotide_map[base]
    return result


def get_reversetranscription(string, reverse=False):
    result = ""
    if not reverse:
        return string.replace("U", "T")
    for base in string[::-1]:
        result += reverse_nucleotide_map[base]
    return result

