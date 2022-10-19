from functools import reduce
from tqdm import tqdm
positions = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def get_prob(kmer, profile):
    return reduce(lambda x, y: x * y,
                  [profile[j][positions[c]]
                   for j, c in enumerate(list(kmer))])


def find_probable_kmer(sequence, k, profile):
    best_kmer, best_prob = sequence[:k], 0
    len_seq=len(sequence) 
    for i in range(len_seq- k + 1):
        kmer = sequence[i: i+k]
        prob = get_prob(kmer, profile)
        if prob > best_prob:
            best_kmer, best_prob = kmer, prob
    return best_kmer

def construct_with_pseudocounts(kmers):
    profile = [[0, 0, 0, 0] for i in range(len(kmers[0]))]
    for kmer in kmers:
        for i, c in enumerate(kmer):
            profile[i][positions[c]] += 1
    for i, freqs in enumerate(profile):
        for f in range(len(freqs)):
            profile[i][f] += 1
            profile[i][f] /= 2 * float(len(kmers))
    return profile

def contruct_profile(kmers):
    profile = [[0, 0, 0, 0] for i in range(len(kmers[0]))]
    for kmer in kmers:
        for i, c in enumerate(kmer):
            profile[i][positions[c]] += 1
    for i, freqs in enumerate(profile):
        for f in range(len(freqs)):
            profile[i][f] /= float(len(kmers))
    return profile


def get_motifs_score(motifs,pseudocounts=False):
    if pseudocounts:
        return (len(motifs[0]) -sum([max(p) for p in construct_with_pseudocounts(motifs)]))
    else:
        return len(motifs[0]) - sum([max(p) for p in contruct_profile(motifs)])

def GreedyMotifSearch(sequence,k,t,pseudocounts=False):
    sequence = [s for s in sequence.split() if s]
    best_score, result = k, []
    len_seq=len(sequence)
    for i in tqdm(range(len(sequence[0]) - k + 1)):
        
        best_motifs = [sequence[0][i:i+k]]
        if pseudocounts:
            profile = construct_with_pseudocounts(best_motifs)
        else:
            profile = contruct_profile(best_motifs)
        for t in range(1, len_seq):
            kmer = find_probable_kmer(sequence[t], k, profile)
            best_motifs.append(kmer)
            if pseudocounts:
                 profile = construct_with_pseudocounts(best_motifs)
            else:
                profile = contruct_profile(best_motifs)

        score = get_motifs_score(best_motifs,pseudocounts)
        if score < best_score:
            best_score, result = score, best_motifs
    print ('best score: %s' %best_score)
    print ('\n'.join(result))