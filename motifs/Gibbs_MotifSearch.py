#!/usr/bin/env python
# coding: utf-8

# Like RandomizedMotifSearch, GibbsSampler starts with randomly chosen k-mers in each of t DNA sequences, but it makes a random rather than a deterministic choice at each iteration. It uses randomly selected k-mers to come up with another set of k-mers.
# RandomizedMotifSearch may change all t strings Motifs in a single iteration. This strategy may prove reckless, since some correct motifs (captured in Motifs) may potentially be discarded at the next iteration. GibbsSampler is a more cautious iterative algorithm that discards a single k-mer from the current set of motifs at each iteration and decides to either keep it or replace it with a new one. This algorithm thus moves with more caution in the space of all motifs.

# In[9]:


import random
from functools import reduce
from biofunctions.motifs.GreedyMotifSearch import get_prob,find_probable_kmer,construct_with_pseudocounts,get_motifs_score
from tqdm import tqdm
def find_gibbs_kmer(sequence, k, profile):
    len_seq=len(sequence)
    probs = [get_prob(sequence[i: i+k], profile) for i in range(len_seq - k + 1)]
    r = random.random() * sum(probs)
    for i, p in enumerate(probs):
        r -= p
        if r < 0:
            idx = i
            break
    return sequence[idx: idx+k]

def Gibbs_MotifSearch(sequence,k,t,n):
    sequence = [s for s in sequence.split() if s]
    len_seq=len(sequence)
    motiflist=[]
    for i in range(len_seq):
        random.seed()
        r = random.randint(0, len(sequence[0]) - k)
        motiflist.append(sequence[i][r: r+k])
    global_best_motifs = motiflist
    global_best_score = get_motifs_score(global_best_motifs,pseudocounts=True)
    
    for y in tqdm(range(20)):
        motiflist=[]
        for i in range(len_seq):
            random.seed()
            r = random.randint(0, len(sequence[0]) - k)
            motiflist.append(sequence[i][r: r+k])
        best_motifs = motiflist
        best_score = get_motifs_score(best_motifs,pseudocounts=True)
        for x in range(n):
            random.seed()
            r = random.randint(0, t - 1)
            profile = construct_with_pseudocounts(motiflist[:r] + motiflist[r+1:])
            motif = find_gibbs_kmer(sequence[r], k, profile)
            motiflist[r] = motif
            score = get_motifs_score(motiflist,pseudocounts=True)
            if score < best_score:
                best_score, best_motifs = score, motiflist
        if best_score < global_best_score:
             global_best_score, global_best_motifs = best_score, best_motifs
                
    print ('global best score: %s' % global_best_score)
    print ('\n'.join(global_best_motifs))

