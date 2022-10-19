#!/usr/bin/env python
# coding: utf-8

# In[16]:

from tqdm import tqdm 
from biofunctions.utils.hamming_distance import hamming_distance
# Find the Motif by using a median string that minimizes hamming distance among all possible choices of k-mers.
def MedianString(sequence,k):
    sequence = [s for s in sequence.split() if s]
    kmerList = []
    for line in tqdm(sequence):
        len_line=len(line)
        String = line
        for i in range(len_line - k+1):
            pattern = line[i:i+k]
            if pattern not in kmerList:
                kmerList.append(pattern)            
        distance = float('inf')
        for kmer in kmerList:
            for i in range(len_line - k+1):
                if distance > hamming_distance(kmer, line[i:i+k]):
                    distance = hamming_distance(kmer, line[i:i+k])
                    Median = kmer
    print(Median)

