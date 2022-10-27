#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The MiddleEdge function below returns middle edge in the alignment graph.
def getscores(seq1, seq2, indel_penality, scoring_matrix):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    previous = [0] * (len_seq1+1)
    current = [0] * (len_seq1+1)
    for i in range(1, len_seq1+1):
        current[i] = current[i-1] - indel_penality

    for j in range(1, len_seq2+1):
        previous = current.copy()
        current[0] = -indel_penality * j
        for i in range(1, len_seq1+1):
            seq1_current = seq1[i-1]
            seq2_current = seq2[j-1]
            deletion = current[i-1] - indel_penality
            insertion = previous[i] - indel_penality
            match_mismatch = previous[i-1] + scoring_matrix[seq1_current][seq2_current]
            current[i] = max(insertion, deletion, match_mismatch)

    result = [[previous[i], current[i]] for i in range(len_seq1+1)] 
    return result


def MiddleEdge(seq1, seq2, indel_penality,scoring_matrix):
    len_seq2 = len(seq2)
    middle_index = len_seq2//2

    score_matrix1 = getscores(seq1, seq2[0:middle_index+1], indel_penality,scoring_matrix)
    score_matrix2 = getscores(seq1, seq2[len_seq2:middle_index-1:-1], indel_penality,scoring_matrix)

    column1 = [score_matrix1[i][0] + score_matrix2[i][1] for i in range(len(seq1)+1)]
    column2 = [score_matrix1[i][1] for i in range(len(score_matrix1))]
    index = column1.index(max(column1))
    insertion = column2[index]

    if index == len(column1) - 1:
        return (index, middle_index), (index, middle_index+1), "H"
    deletion = column1[index + 1]
    match_mismatch = column2[index + 1]
    value = max(insertion, deletion, match_mismatch)

    if value == insertion:
        return (index, middle_index), (index, middle_index+1), "H"
    elif value == deletion:
        return (index, middle_index), (index+1, middle_index), "V"
    else:
        return (index, middle_index), (index+1, middle_index+1),"D"
