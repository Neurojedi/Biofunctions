#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Randomized Motif Search Algorithm
from biofunctions.motifs.GreedyMotifSearch import get_prob,find_probable_kmer,construct_with_pseudocounts,get_motifs_score
import random
from tqdm import tqdm
def Randomized_MotifSearch(sequence,k,t):
    sequence = [s for s in sequence.split() if s]
    len_seq=len(sequence)
    motiflist=[]
    for i in range(len_seq):
        random.seed()
        r = random.randint(0, len(sequence[0]) - k)
        motiflist.append(sequence[i][r: r+k])
    global_best_motifs = motiflist
    global_best_score = get_motifs_score(global_best_motifs,pseudocounts=True)
    for t in tqdm(range(1000)):
        motiflist=[]
        for i in range(len_seq):
            random.seed()
            r = random.randint(0, len(sequence[0]) - k)
            motiflist.append(sequence[i][r: r+k])
        best_motifs = motiflist
        best_score = get_motifs_score(best_motifs,pseudocounts=True)
        for x in range(10000):
            profile = construct_with_pseudocounts(motiflist)
            motiflist = [find_probable_kmer(d, k, profile) for d in sequence]
            score = get_motifs_score(motiflist,pseudocounts=True)
            if score < best_score:
                best_score, best_motifs = score, motiflist
            else:
                break
        if best_score < global_best_score:
             global_best_score, global_best_motifs = best_score, best_motifs
                
    print ('global best score: %s' % global_best_score)
    print ('\n'.join(global_best_motifs))

