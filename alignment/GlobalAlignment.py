#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Output:The maximum alignment score of these strings followed by an alignment achieving this maximum score.
def GlobalAlignment(seq1,seq2,indel_penality,scoring_matrix):
    seq1 = '-' + seq1
    seq2 = '-' + seq2
    
    S = [[0 for i in range(len(seq2))] for j in range(len(seq1))]
    Backtrack = [[0 for i in range(len(seq2))] for j in range(len(seq1))]
    for i in range(1, len(S)):
        S[i][0] = S[i - 1][0] - indel_penality
        Backtrack[i][0] = 1
    for j in range(1, len(S[0])):
        S[0][j] = S[0][j - 1] - indel_penality
        Backtrack[0][j] = 2
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            diag = S[i - 1][j - 1] + scoring_matrix[seq1[i]][seq2[j]]
            down = S[i - 1][j] - indel_penality
            right = S[i][j - 1] - indel_penality
            S[i][j] = max([down, right, diag])
            if S[i][j] == down:
                Backtrack[i][j] = 1
            elif S[i][j] == right:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4

    print(S[len(seq1) - 1][len(seq2) - 1])
    return Backtrack

def Alignment(Backtrack, seq1, seq2):
    i = len(Backtrack) - 1
    j = len(Backtrack[0]) - 1
    res_seq1 = ''
    res_seq2 = ''
    while i > 0 or j > 0:
        if Backtrack[i][j] == 4:
            res_seq1 = seq1[i - 1] + res_seq1
            res_seq2 = seq2[j - 1] + res_seq2
            i -= 1
            j -= 1
        elif Backtrack[i][j] == 2:
            res_seq1 = '-' + res_seq1
            res_seq2 = seq2[j - 1] + res_seq2
            j -= 1
        else:
            res_seq1 = seq1[i - 1] + res_seq1
            res_seq2 = '-' + res_seq2
            i -= 1
    print(res_seq1)
    print(res_seq2)

