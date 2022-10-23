#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns DeBruijnk(Text), in the form of an adjacency list
from collections import defaultdict
from biofunctions.assembly.Composition import composition
def build_debruijn_from_string(sequence, k):
    nodes = composition(sequence, k-1, False)
    edges = defaultdict(list)
    len_seq=len(sequence)
    for i in range(len_seq-k+1):
        edges[nodes[i]].append(nodes[i+1])
    return edges
def get_debruijn_graph(graph):
    return '\n'.join([
        f'{key} -> {",".join(values)}' # For Bioinformatics Course, you should use : instead of ->
        for key, values in graph.items()
    ])  

def prefix(kmer):
    return kmer[:-1]

def suffix(kmer):
    return kmer[1:]

def build_debruijn_from_kmers(kmers):
    edges = defaultdict(list)
    for kmer in kmers:
        edges[prefix(kmer)].append(suffix(kmer))
    return edges