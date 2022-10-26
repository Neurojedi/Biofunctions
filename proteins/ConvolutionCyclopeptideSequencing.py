#!/usr/bin/env python
# coding: utf-8

# In[16]:

#Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).
from collections import defaultdict
from biofunctions.proteins.SpectrumConvolution import SpectrumConvolution
from biofunctions.proteins.LeaderboardCyclopeptideSequencing import LeaderboardCyclopeptideSequencing_Long
def ConvolutionCyclopeptideSequencing(spectrum, m, n):
    spectrum=sorted(spectrum)
    convolutions = SpectrumConvolution(spectrum)
    convolutions_pruned = get_TopConvolutions(convolutions, m)
    leader_spectrum = LeaderboardCyclopeptideSequencing_Long(spectrum, convolutions_pruned, n)
    return leader_spectrum

def get_TopConvolutions(convolutions, m):
    convolutions = list(filter(lambda x: x >= 57 and x <= 200, convolutions))
    convolutions_count = defaultdict(int)
    result_convolutions = []
    count = 0
    for spectrum in convolutions:
        convolutions_count[spectrum] += 1
    count_list = defaultdict(list)
    for spectrum, count in convolutions_count.items():
        count_list[count].append(spectrum)
    sorted_counts = sorted(count_list.keys())
    place = len(sorted_counts) - 1
    while count < m:
        key = sorted_counts[place]
        result_convolutions += count_list[key]
        count+= len(count_list[key])
        place-=1
    result_convolutions=sorted(result_convolutions)
    return result_convolutions

def get_Highest(peptides, count,m):
    spectrums = []
    sorted_keys = sorted(peptides.keys())
    count = 0
    len_keys=len(sorted_keys)
    place = len_keys - 1
    while count < m:
        key = sorted_keys[place]
        spectrums += peptides[key]
        count+= len(peptides[key])
        place-=1
    spectrums = spectrums[:count]
    spectrums=sorted(spectrums)
    return spectrums