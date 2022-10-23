#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns the collection of all maximal nonbranching paths in this graph.

from collections import defaultdict
from biofunctions.assembly.ContigGeneration import getInstance,check

def MaximalNonBranchingPaths(output_graph):
    result_list = []
    ins = getInstance(output_graph)
    complete_list = {}
    for kmer in list(output_graph.keys()):
        complete_list[kmer] = False
        outs = output_graph[kmer]
        if not check(kmer, ins, output_graph):
            complete_list[kmer] = True
            contigs = [[kmer] for i in outs]
            for i, out in enumerate(outs):
                complete_list[kmer] = True
                current = out
                contigs[i].append(current)
                while check(current, ins, output_graph):
                    complete_list[kmer] = True
                    current = output_graph[current][0]
                    contigs[i].append(current)
            result_list += contigs

    selected_cycles = []
    for kmer in list(output_graph.keys()):
        cycle = []
        current = kmer
        if kmer not in complete_list or complete_list[kmer]:
            continue
        while check(current, ins, output_graph):
            cycle.append(current)
            current = output_graph[current][0]
            complete_list[current] = True
            if current == kmer:
                cycle.append(kmer)
                selected_cycles.append(cycle)
                break

    return result_list + selected_cycles

