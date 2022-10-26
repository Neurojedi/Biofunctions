#!/usr/bin/env python
# coding: utf-8

# In[16]:


#The function below returns all substrings of Text encoding Peptide
from biofunctions.proteins.Translate import get_translation
from biofunctions.proteins.Transcribe import get_reversetranscription,get_transcription
def PeptideEncoding(nucleotide_list, target):
    nucleotide_length = len(target) * 3
    result = []
    rna = get_transcription(nucleotide_list)
    compliment_rna = get_transcription(nucleotide_list, True)
    len_rna=len(rna)
    for i in range(len_rna - nucleotide_length):
        rna_segment = rna[i: nucleotide_length+i]
        peptide = get_translation(rna_segment)
        if peptide == target:
            result.append(get_reversetranscription(rna_segment))
    len_comprna=len(compliment_rna)
    for i in range(len_comprna - nucleotide_length-1, -1, -1):
        rna_segment = compliment_rna[i: nucleotide_length+i]
        peptide = get_translation(rna_segment)
        if peptide == target:
            result.append(get_reversetranscription(rna_segment, True))

    return result

