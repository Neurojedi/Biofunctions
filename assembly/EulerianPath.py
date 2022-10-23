#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns an Eulerian path in this graph.
from random import choice
from collections import defaultdict

def initialize(cycles):
    result  = dict()
    for k, j in cycles.items():
        if k not in result != 2:
            result[k] = [0, 0]
        result[k][0] = len(j)
        for t in j:
            if t not in result != 2:
                result[t] = [0, 0]
            result[t][1]+=1
    for i, edges in result.items():
        if edges[0] > edges[1]:
            return i
    return list(result.keys())[0]

def get_EulerianPath(sequence):
    cycles = defaultdict(list)
    for line in sequence:
        chars = list(map(lambda x: x.strip(), line.split(':')))
        cycles[chars[0]] = chars[1].split(' ')
    result = []
    cycle_list = [initialize(cycles)]
    while len(cycle_list) > 0:
        current = cycle_list[-1]
        if len(cycles[current]) == 0:
            result.insert(0, cycle_list.pop())
        else:
            cycle_list.append(cycles[current].pop())
    return print(*result)

