#!/usr/bin/env python
# coding: utf-8

# In[1]:

#The function below returns the desired output for Longest Path along Directed Acyclic Graph
from collections import defaultdict, OrderedDict

def LongestPathDAG(in_graph, out_graph, start, last):
    maximums = defaultdict(int)
    queue = []
    degree_list = []
    for node in in_graph.keys():
        if node not in out_graph and node != start:
            degree_list.append(node)
    while len(degree_list):
        node = degree_list.pop(0)
        if node not in in_graph:
            continue
        outputs = list(in_graph[node].keys())
        in_graph.pop(node)
        for i in outputs:
            if len(out_graph[out]) == 1:
                degree_list.append(i)
            out_graph[i].pop(node)
    topological_list = []
    in_degrees = defaultdict(int)
    for i in in_graph.keys():
        in_degrees[i] = 0
    for i, j in out_graph.items():
        in_degrees[i] = len(j.keys())

    topological_queue = []
    for node, in_degree in in_degrees.items():
        if in_degree == 0:
            topological_queue.append(node)
    while len(topological_queue):
        node = topological_queue.pop(0)
        topological_list.append(node)
        if node not in in_graph:
            continue
        for i in in_graph[node].keys():
            in_degrees[i] -= 1
            if in_degrees[i] == 0:
                topological_queue.append(i)

    for node in topological_list:
        max_value = 0
        for i, j in out_graph[node].items():
            max_value = max(
                maximums[i] + j, max_value
            )
        maximums[node] = max_value

    current = last
    while current != start:
        queue.append(current)
        out_weights = out_graph[current]
        max_out, max_weight = 0, 0
        for i, j in out_weights.items():
            if maximums[i] + j > max_weight:
                max_weight = maximums[i] + j
                max_out = i
            current = max_out
    queue.append(start)
    queue.reverse()
    return maximums[last], queue 
