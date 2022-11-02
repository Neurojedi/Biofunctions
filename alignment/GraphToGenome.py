#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Output: The genome P corresponding to this genome graph.(The implementation below is for assignment of the Course and I used an altered version in TwoBreakSorting)
from biofunctions.alignment.get_chromosome import get_chromosome
def GraphToGenome(GenomeGraph):
    GenomeGraph = GenomeGraph[1:-1]
    GenomeGraph = GenomeGraph.split('), (')
    for i in range(len(GenomeGraph)):
        GenomeGraph[i] = GenomeGraph[i].split(', ')
        for j in range(len(GenomeGraph[i])):
            GenomeGraph[i][j] = int(GenomeGraph[i][j])
    result = []
    cycle_list = []
    elements = []
    len_Graph=len(GenomeGraph)
    for i in range(len_Graph):
        if i == len_Graph - 1:
            elements += GenomeGraph[i]
            cycle_list.append(elements)
        elif GenomeGraph[i][1] == GenomeGraph[i + 1][0] + 1 or GenomeGraph[i][1] == GenomeGraph[i + 1][0] -1:
            elements += GenomeGraph[i]
        else:
            elements += GenomeGraph[i]
            cycle_list.append(elements)
            elements = []
    for i in cycle_list:
        chromosome = get_chromosome([i[-1]] + i[:-1])
        result.append(chromosome)
    for j in range(len(result)):
        result[j] = '(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result[j]) + ')'
    print(''.join(result))

if __name__ == "__main__":
    inp="(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
    result = GraphToGenome(inp)

