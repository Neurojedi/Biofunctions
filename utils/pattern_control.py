from biofunctions.utils.hamming_distance import hamming_distance
def pattern_control(pattern, sequence, d):
    position = []
    lenseq=len(sequence)
    lenpat=len(pattern)
    for i in range (lenseq - lenpat+1):
        if hamming_distance(pattern, sequence[i:i + lenpat]) <= int(d):
            return True
    return False   