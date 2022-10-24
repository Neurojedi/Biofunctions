#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Output: A highest-scoring fitting alignment between v and w. Use the BLOSUM62 scoring table
def FittingAlignment(seq1, seq2, indel_penalty, scoring_matrix):
    s = []
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    S=[[0 for x in range(len_seq2+1)] for x in range(len_seq1+1)] 
    for i in range(0, len_seq1 + 1):
        for j in range(0, len_seq2 + 1):
            if j == 0:
                S[i][j] = 0
            elif i == 0:
                S[i][j] = j * indel_penalty
            else:
                S[i][j] = max(S[i-1][j-1] + scoring_matrix[seq1[i-1]][seq2[j-1]], S[i-1][j] + indel_penalty, S[i][j-1] + indel_penalty)
    max_value = 0
    s1=0
    s2=0
    for j in range(0, len_seq1+1):
        val = S[j][len_seq2]
        if val > max_value:
            max_value = val
            s1=j
    i = s1
    j = len_seq2
    list_seq1 = []
    list_seq2 = []
    score = max_value
    while score >= 0 and i > 0 and j > 0:
        if S[i][j] == S[i-1][j-1] + scoring_matrix[seq1[i-1]][seq2[j-1]]:
            list_seq1.append(seq1[i-1])
            list_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
            score = S[i][j]
        elif S[i][j] == S[i-1][j] + indel_penalty:
            list_seq1.append(seq1[i-1])
            list_seq2.append('-')
            i -= 1
            score = S[i][j]
        elif S[i][j] == S[i][j-1] + indel_penalty:
            list_seq1.append('-')
            list_seq2.append(seq2[j-1])
            j -= 1
            my_score = S[i][j]
    k = ''.join(list_seq1[::-1])
    l = ''.join(list_seq2[::-1])
    return max_value, k, l

