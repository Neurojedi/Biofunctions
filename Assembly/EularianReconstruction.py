#!/usr/bin/env python
# coding: utf-8

# In[1]:

# The function below returns string construction using Eulerian Cycles and de Bruijn Graph
from random import choice
from collections import defaultdict
from biofunctions.assembly.EulerianPath import initialize
from biofunctions.assembly.DeBruijnGraph import build_debruijn_from_kmers, get_debruijn_graph


def get_EulerianPath(cycles):
    
    result = []
    cycle_list  = [initialize(cycles)]
    while len(cycle_list) > 0:
        current = cycle_list[-1]
        if len(cycles[current]) == 0:
            
            result.insert(0, cycle_list.pop())
        else:
            cycle_list.append(cycles[current].pop())
    
    return result
                              
def genome_to_path(motifs):
    pick = motifs[0]
    len_motif=len(motifs)
    for i in range(1, len_motif):
        pick += motifs[i][-1]
    return pick

def StringReconstruction(kmers):
    db = build_debruijn_from_kmers(kmers)
    path = get_EulerianPath(db)
    pt=genome_to_path(path)
    return pt
