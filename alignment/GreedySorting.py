#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Output: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.
def get_sorted(P, i):
    j = i
    while P[j] != i + 1 and P[j] != -(i + 1):
        j += 1
    P[i:j+1] = list(map(lambda x: -x, P[i:j+1][::-1]))
    return P

def GreedySorting(P):
    P = P.split(' ')
    for i in range(len(P)):
        P[i] = int(P[i])
    reversals = []
    len_p=len(P)
    for i in range(len_p):
        while P[i] != i + 1:
            result = get_sorted(P, i)
            reversals.append(list(result))
    for r in reversals:
        print(' '.join(('+' if i > 0 else '')+str(i) for i in r))

