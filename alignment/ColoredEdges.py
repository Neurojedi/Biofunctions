#!/usr/bin/env python
# coding: utf-8

# In[1]:


from biofunctions.alignment.get_cycle import get_cycle
def ColoredEdges(Chromosome):
    edge_list = []
    for element in Chromosome:
        node = get_cycle(element)
        len_node=len(node)
        for i in range(1, len_node, 2):
            if i != len_node - 1:
                edge_list.append([node[i], node[i + 1]])
            else:
                edge_list.append([node[i], node[0]])
    return edge_list
