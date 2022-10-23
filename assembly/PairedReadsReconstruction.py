#!/usr/bin/env python
# coding: utf-8

# In[1]:

# The function returns a string Text with (k, d)-mer composition equal to PairedReads.
from biofunctions.assembly.EularianReconstruction import get_EulerianPath
from collections import defaultdict
def DeBruijnPairedKmers(pairs):
    mapping = defaultdict(list)
    for kmers in pairs:
        prefix = "{}|{}".format(kmers[0][:-1], kmers[1][:-1])
        suffix = "{}|{}".format(kmers[0][1:], kmers[1][1:])
        mapping[prefix].append(suffix)
    return mapping
def ConstructPairedGenomePath(pairs, k, d):
    len_pairs = len(pairs)
    result = ['*'] * (2*k + len_pairs - 1)
    l = k - 1
    for i, pair in enumerate(pairs):
        prefix, suffix = pair.split('|')
        summing = i+k+d
        result[i:i+l] = list(prefix)
        result[summing:summing+l] = list(suffix)
    return "".join(result)
def get_PairedReconstruction(pairs, n, d):
    graph = DeBruijnPairedKmers(pairs)
    path = get_EulerianPath(graph)
    return ConstructPairedGenomePath(path, n, d)

