#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of v and a prefix w' of w achieving this maximum score.
def OverlapAlignment(seq1, seq2, penality):
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
    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            symbol_a = seq1[i-1]
            symbol_b = seq2[j-1]
            match = -2
            if symbol_a == symbol_b:
                match = 1
            ins = S[i-1][j] - penality
            dels = S[i][j-1] - penality
            match_mismatch = S[i-1][j-1] + match

            S[i][j] = max(ins, dels, match_mismatch)

            if S[i][j] == ins:
                backtrack[i][j] = "|"
            elif S[i][j] == dels:
                backtrack[i][j] = "-"
            elif S[i][j] == match_mismatch:
                backtrack[i][j] = "+"

    max_val = S[0][-1]
    max_index = 0
    for j in range(len_seq2+1):
        if S[-1][j] >= max_val:
            max_val = S[-1][j]
            max_index = j


    result_seq1 = ""
    result_seq2 = ""
    i, j = len_seq1, max_index
    while i > 0 and j > 0:
        if backtrack[i][j] == "0":
            return max_val, result_seq1, result_seq2
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

    return max_val, result_seq1, result_seq2

