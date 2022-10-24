#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns the length of a longest path in the Manhattan Tourist Problem
def MahattanTourist(x, k, d, r):
    longest_path = [[0] * (k+1) for i in range(x+1)]
    for i in range(1, x+1):
        longest_path[i][0] = longest_path[i-1][0] + d[i-1][0]
    for i in range(1, k+1):
        longest_path[0][i] = longest_path[0][i-1] + r[0][i-1]
    for i in range(1, x+1):
        for j in range(1, k+1):
            longest_path[i][j] = max(
                longest_path[i-1][j] + d[i-1][j],
                longest_path[i][j-1] + r[i][j-1]
            )
    return longest_path[x][k]
