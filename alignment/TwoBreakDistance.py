#!/usr/bin/env python
# coding: utf-8

# In[1]:

#The function below return the 2-break distance.
from biofunctions.alignment.get_cycle import get_cycle
from biofunctions.alignment.ColoredEdges import ColoredEdges

def get_processed(string):
    string = string[1:-1]
    string = string.split(')(')
    len_string=len(string)
    for i in range(len_string):
            string[i] = string[i].split(' ')
            for j in range(len(string[i])):
                string[i][j] = int(string[i][j])
    return string


def get_next(current_item, edge):
    idx = 0
    len_edge=len(edge)
    if len_edge == 0:
        return -1
    while not (current_item[0] in edge[idx] or current_item[1] in edge[idx]):
        idx += 1
        if idx == len_edge:
            return -1
    return edge[idx]


def TwoBreakDistance(P, Q):
    P=get_processed(P)
    Q=get_processed(Q)
    edgesP = ColoredEdges(P)
    edgesQ = ColoredEdges(Q)
    sum_edges = edgesP + edgesQ
    block_set = set()
    for i in sum_edges:
        block_set.add(i[0])
        block_set.add(i[1])
    cycle_list = []
    while len(sum_edges) != 0:
        ground = sum_edges[0]
        sum_edges.remove(sum_edges[0])
        cycle = [ground]
        current = get_next(ground, sum_edges)
        while current != -1:
            cycle.append(current)
            sum_edges.remove(current)
            current = get_next(current, sum_edges)
        cycle_list.append(cycle)
    return len(block_set) // 2 - len(cycle_list)

