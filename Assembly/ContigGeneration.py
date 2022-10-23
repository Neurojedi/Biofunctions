#!/usr/bin/env python
# coding: utf-8

# In[1]:

# The function below (get_Contig) returns all contigs in DeBruijn Graph.
import sys
import os
from collections import defaultdict
from biofunctions.assembly.DeBruijnGraph import build_debruijn_from_kmers


def getInstance(graph):
    instance = defaultdict(list)
    for kmer, outputs in graph.items():
        for out in outputs:
            instance[out].append(kmer)
    return instance

def check(kmer, ins, outs):
    return len(ins[kmer]) == len(outs[kmer]) == 1

def get_Contig(kmers):
    result = []
    out_graph = build_debruijn_from_kmers(kmers)
    in_graph = getInstance(out_graph)
    for kmer in list(out_graph.keys()):
        outs = out_graph[kmer]
        if not check(kmer, in_graph, out_graph):
            contig_list = [kmer] * len(outs)
            for i, out in enumerate(outs):
                current = out
                contig_list[i] += current[-1]
                while check(current, in_graph, out_graph):
                    current = out_graph[current][0]
                    contig_list[i] += current[-1]
            result += contig_list

    return result


