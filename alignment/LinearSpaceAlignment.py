#!/usr/bin/env python
# coding: utf-8

# In[1]:

from biofunctions.utils.ScoringMatrix import BLOSUM62
from biofunctions.alignment.MiddleEdge import MiddleEdge 

# Output: The maximum alignment score of these strings, followed by an alignment achieving this maximum score.
def ModifiedMiddleEgde(seq1, seq2, top, bottom, left, right, penality, scoring_matrix):
    mid_node, next_node, direction = MiddleEdge(seq1[top:bottom], seq2[left:right], penality, scoring_matrix) 
    return (mid_node[0]+top, mid_node[1]+left), (next_node[0]+top, next_node[1]+left), direction

def LinearSpaceAlignment(seq1, seq2, top, bottom, left, right, penality, stack, scoring_matrix):
    if left == right:
        stack.append((bottom - top) * "V")
    elif top == bottom:
        stack.append((left - right) * "H")
    else:
        mid_node, next_node, direction = ModifiedMiddleEgde(seq1, seq2, top, bottom, left, right, penality, scoring_matrix)
        LinearSpaceAlignment(seq1, seq2, top, mid_node[0], left, mid_node[1], penality, stack,scoring_matrix)
        stack.append(direction)
        LinearSpaceAlignment(seq1, seq2, next_node[0], bottom, next_node[1], right, penality, stack,scoring_matrix)

def OutputLCS(backtrack, seq1, seq2):
    seq1_result = "" 
    seq2_result = "" 
    seq1_index = 0
    seq2_index = 0
    for i, direction in enumerate(backtrack):
        if direction == "D":
            seq1_result += seq1[seq1_index]
            seq2_result += seq2[seq2_index]
            seq1_index += 1
            seq2_index += 1
        elif direction == "H":
            seq1_result += seq1[seq1_index]
            seq2_result += "-"
            seq1_index += 1
        else:
            seq1_result += "-"
            seq2_result += seq2[seq2_index]
            seq2_index += 1
    return seq1_result, seq2_result

