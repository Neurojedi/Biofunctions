#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Output: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score.
def AffineGapPenalties(seq1, seq2, gap_opening, gap_extension, scoring_matrix):
    m1 = []
    m2 = []
    m3 = []
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    m1, m2, m3 = [[0 for x in range(len_seq2+1)] for x in range(len_seq1+1)], [[0 for x in range(len_seq2+1)] for x in range(len_seq1+1)], [[0 for x in range(len_seq2+1)] for x in range(len_seq1+1)]  
    for i in range(1, len_seq1+1):
        m1[i][0] = gap_opening + (i-1)*gap_extension
        m2[i][0] = gap_opening + (i-1)*gap_extension
        m3[i][0] = float('-inf')
    for j in range(1, len_seq2+1):
        m3[0][j] = gap_opening + (j-1)*gap_extension
        m2[0][j] = gap_opening + (j-1)*gap_extension
        m1[0][j] = float('-inf')

    for i in range(1, len_seq1+1):
        for j in range(1, len_seq2+1):
            m1[i][j] = max(m1[i-1][j] + gap_extension, m2[i-1][j] + gap_opening)
            m3[i][j] = max(m3[i][j-1] + gap_extension, m2[i][j-1] + gap_opening)
            m2[i][j] = max(m1[i][j], m2[i-1][j-1] + scoring_matrix[seq1[i-1]][seq2[j-1]], m3[i][j])
    k = []
    l = []
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    score = max(m1[len_seq1][len_seq2], m2[len_seq1][len_seq2], m3[len_seq1][len_seq2])
    current = []
    if score == m1[len_seq1][len_seq2]:
        current = m1
    elif score == m2[len_seq1][len_seq2]:
        current = m2
    else:
        current = m3
    while len_seq1 > 0 and len_seq2 > 0:
        if current == m1:
            if m1[len_seq1][len_seq2] == m1[len_seq1-1][len_seq2] + gap_extension:
                k.append(seq1[len_seq1-1])
                l.append('-')
                len_seq1 -= 1
                current = m1 
            elif m1[len_seq1][len_seq2] == m2[len_seq1-1][len_seq2] + gap_opening:
                k.append(seq1[len_seq1-1])
                l.append('-')
                len_seq1 -= 1
                current = m2
        elif current == m2:
            if m2[len_seq1][len_seq2] == m1[len_seq1][len_seq2]:
                current = m1
            elif m2[len_seq1][len_seq2] == m2[len_seq1-1][len_seq2-1] + scoring_matrix[seq1[len_seq1-1]][seq2[len_seq2-1]]:
                k.append(seq1[len_seq1-1])
                l.append(seq2[len_seq2-1])
                len_seq1 -= 1
                len_seq2 -= 1
                current = m2
            elif m2[len_seq1][len_seq2] == m3[len_seq1][len_seq2]:
                current = m3
        elif current == m3:
            if m3[len_seq1][len_seq2] == m3[len_seq1][len_seq2-1] + gap_extension:
                k.append('-')
                l.append(seq2[len_seq2-1])
                len_seq2 -= 1
                current = m3
            elif m3[len_seq1][len_seq2] == m2[len_seq1][len_seq2-1] + gap_opening:
                k.append('-')
                l.append(seq2[len_seq2-1])
                len_seq2 -= 1
                current = m2

    while len_seq1 > 0:
        k.append(seq1[len_seq1-1])
        l.append('-')
        len_seq1 -= 1
    while len_seq2 > 0:
        k.append('-')
        l.append(seq2[len_seq2-1])
        len_seq2 -= 1
    k = ''.join(k[::-1])
    l = ''.join(l[::-1])
    return score, k , l