#!/usr/bin/env python
# coding: utf-8

# In[58]:


# The function below returns all most frequent k-mers with up to d mismatches in Text.
import itertools
import time
from collections import defaultdict

def frequentkmerswithmismatch(sequence, k, d):
    frequent_list = []
    frequencies = defaultdict(lambda: 0)
    n=len(sequence)
    for index in range(n - k + 1):
        curr_kmer_and_permutations = PermuteMotifDistanceTimes(sequence[index : index + k], d)
        for kmer in curr_kmer_and_permutations:
            frequencies[kmer] += 1 

    for kmer in frequencies:
        if frequencies[kmer] == max(frequencies.values()):
            frequent_list.append(kmer)
    return print(*frequent_list)

def PermuteMotifOnce(kmers, nucleotides={"A", "C", "G", "T"}):
    return list(set(itertools.chain.from_iterable([[
        kmers[:pos] + nucleotide + kmers[pos + 1:] for
        nucleotide in nucleotides] for
        pos in range(len(kmers))])))


def PermuteMotifDistanceTimes(kmers, d):
    workingSet = {kmers}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
    return list(workingSet)

