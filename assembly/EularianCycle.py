#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns EulerianCycle
from random import choice
from collections import defaultdict

def get_EulerianCycle(sequence):
    cycles = defaultdict(list)
    for line in sequence:
        chars = list(map(lambda x: x.strip(), line.split(':')))
        cycles[chars[0]] = chars[1].split(' ')
    result = []
    cycle_list = [choice(list(cycles.keys()))]
    while len(cycle_list) > 0:
        current = cycle_list[-1]
        if len(cycles[current]) == 0:
            result.insert(0, cycle_list.pop())
        else:
            cycle_list.append(cycles[current].pop())
    return print(*result)

