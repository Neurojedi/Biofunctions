#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Output: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score.
def LocalAlignment(seq1, seq2, penality,scoring_matrix):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    S = [[0] * (len_seq2+1) for i in range(len_seq1+1)]
    backtrack = [[0] * (len_seq2+1) for i in range(len_seq1+1)]
    for i in range(1, len_seq1+1):
        S[i][0] = 0
        backtrack[i][0] = seq1[i-1]
    for j in range(1, len_seq2+1):
        S[0][j] = 0
        backtrack[0][j] = seq2[j-1]

    max_value = 0
    max_i, max_j = 0, 0
    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            symbol_s1 = seq1[i-1]
            symbol_s2 = seq2[j-1]
            match = scoring_matrix[symbol_s1][symbol_s2]

            free_ride = 0
            insertion = S[i-1][j] - penality
            deletion = S[i][j-1] - penality
            match_mismatch = S[i-1][j-1] + match

            S[i][j] = max(free_ride, insertion, deletion, match_mismatch)
            if S[i][j] == free_ride:
                backtrack[i][j] = "0"
            elif S[i][j] == insertion:
                backtrack[i][j] = "|"
            elif S[i][j] == deletion:
                backtrack[i][j] = "-"
            elif S[i][j] == match_mismatch:
                backtrack[i][j] = "+"
            
            if S[i][j] > max_value:
                max_value = S[i][j]
                max_i = i
                max_j = j

    result_seq1 = ""
    result_seq2 = ""
    i, j = max_i, max_j
    while i > 0 and j > 0:
        if backtrack[i][j] == "0":
            return max_value, result_seq1, result_seq2
        if backtrack[i][j] == "+":
            result_seq1 = seq1[i-1] + result_seq1 
            result_seq2 = seq2[j-1] + result_seq2
            i-=1
            j-=1
        elif backtrack[i][j] == "|":
            result_seq1 = seq1[i-1] + result_seq1
            result_seq2 = "-" + result_seq2
            i-=1
        elif backtrack[i][j] == "-":
            result_seq1 = "-" + result_seq1
            result_seq2 = seq2[j-1] + result_seq2
            j-=1
    if i > 0:
        result_seq1 = seq1[i-1] + result_seq1 
        result_seq2 = "-" + result_seq2
    if j > 0:
        result_seq2 = seq2[j-1] + result_seq2 
        result_seq1 = "-" + result_seq1

    return max_value, result_seq1, result_seq2






