#!/usr/bin/env python
# coding: utf-8

# In[1]:

from collections import Counter
import copy
import random
import sys
import numpy as np
from biofunctions.alignment.get_cycle import get_cycle
from biofunctions.alignment.ColoredEdges import ColoredEdges
from biofunctions.alignment.TwoBreakDistance import TwoBreakDistance
# Output: The sequence of genomes resulting from applying a shortest sequence of 2-breaks transforming one genome into the other.
def TwoBreakSorting(P, Q):
    edges_P=get_processededges(P)
    edges_Q=get_processededges(Q)
    colored_edges = ColoredEdges([edges_Q])
    seq = []
    seq.append(edges_P)
    P = [edges_P]
    Q = [edges_Q]
    while TwoBreakDistance(P, Q, False) > 0:
        cycles = get_numcycles(ColoredEdges(P), colored_edges)
        for i in cycles:
            if len(i) >= 4:
                get_edge=ColoredEdges(P)
                genome_graph=TwoBreakOnGenomeGraph(get_edge, i[0], i[1], i[3], i[2])
                P = GraphToGenome(genome_graph)
                seq.append(P)
    genome = []
    for c in seq:
        if len(c) >= 4 and type(c[0]) == int:
            elements = []
            for i in c:
                if i > 0:
                    elements.append('+' + str(i))
                else:
                    elements.append(str(i))
            result = ' '.join(elements)
            result = '(' + result + ')'
            genome.append(result)
        else:
            newline = ''
            for i in c:
                elements = []
                for j in i:
                    if j > 0:
                        elements.append('+' + str(j))
                    else:
                        elements.append(str(j))
                result = ' '.join(elements)
                result = '(' + result + ')'
                newline += result
            genome.append(newline)
    for i in genome:
        print(i)

def get_numcycles(P,Q):
    list_cycles = []
    len_sum = len(P)+len(Q) 
    m_ground = np.zeros(shape = len_sum, dtype = bool)
    m_adj = np.zeros(shape = (len_sum,2), dtype = np.int32)
    for i in P:
        m_adj[i[0]-1,0] = i[1]-1
        m_adj[i[1]-1,0] = i[0]-1
    for i in Q:
        m_adj[i[0]-1,1] = i[1]-1
        m_adj[i[1]-1,1] = i[0]-1
    for node in range(len_sum):
        if not m_ground[node]:
            m_ground[node] = True
            top = node
            cycle = [top+1]
            counter = 0
            while (True):
                node = m_adj[node,counter]
                if (node == top):
                    list_cycles.append(cycle)
                    break
                cycle.append(node+1)
                m_ground[node] = True
                counter = (counter+1) % 2
    return list_cycles
def GraphToGenome(genome_graph):
    P = []
    i = 0
    ground_list = []
    m_adj = np.zeros(len(genome_graph)*2, dtype = np.int32)
    for j in genome_graph:
        m_adj[j[0]-1] = j[1]-1
        m_adj[j[1]-1] = j[0]-1
    for j in genome_graph:
        first = j[0]
        if first in ground_list:
            continue
        ground_list.append(first)
        if first%2 == 0:
            selected = first - 1
        else:
            selected = first + 1
        chromosomes = []
        while True:
            if first%2 == 0:
                chromosomes.append(first//2)
            else:
                chromosomes.append(-(first+1)//2)
            next_adj = m_adj[first-1]+1
            ground_list.append(next_adj)
            if next_adj == selected:
                P.append(chromosomes)
                break
            if next_adj%2 == 0:
                first = next_adj - 1
            else:
                first = next_adj + 1
            ground_list.append(first)
    genome = []
    for chromosome in P:
        genome.append([chromosome.pop()] + chromosome)
    return genome

def TwoBreakOnGenomeGraph(genome_graph, x, y, z, m):
    com = [(x, y), (y, x), (z, m), (m, z)]
    graph = [i for i in genome_graph if i not in com]
    graph.append((x, z))
    graph.append((y, m))
    return graph
def get_processededges(P):
    edges = []
    for i in P:
        if i[0] == '-':
            i = -1*int(i[1:])
        else:
            i = int(i[1:])
        edges.append(i)
    return edges

