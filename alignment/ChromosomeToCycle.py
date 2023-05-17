#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Output: The chromosome Chromosome containing n synteny blocks resulting from applying CycleToChromosome to Nodes.
def get_chromosome(nodes,fancy=False):
    if fancy:
        nodes=nodes[1:-1]
        nodes=nodes.split(' ')
        for i in range(len(nodes)):
            nodes[i] = int(nodes[i])
    node_list = []
    counter = 0
    while counter < len(nodes):
        if nodes[counter] < nodes[counter+1]:
            node_list.append(nodes[counter+1]//2)
        else:
            node_list.append(-nodes[counter+1]//2)
        counter += 2
    if fancy:
        print('(' + ' '.join(('+' if i > 0 else '') + str(i) for i in node_list) + ')')
    else:
        return node_list
