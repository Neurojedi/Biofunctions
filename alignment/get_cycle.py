#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_cycle(sequence): 
    node_list = []
    for target in sequence:
        if target > 0:
            node_list.append(2 * target - 1)
            node_list.append(2 * target)
        else:
            node_list.append(-2 * target)
            node_list.append(-2 * target - 1)
    return node_list
