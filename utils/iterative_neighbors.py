def ImmediateNeighbors(pattern):
    neighbors = set()
    nucleotides = {'A', 'C', 'G', 'T'}
    len_pat=len(pattern)
    for i in range(len_pat):
        for n in nucleotides:
            neighbors.add(pattern[:i]+n+pattern[i+1:])
    return neighbors

def iterative_neighbors(pattern, d):
    if d == 0:
        return {pattern}
    imneighbor = ImmediateNeighbors(pattern)
    neighbor = imneighbor
    for j in range(d-1):
        for p in imneighbor:
            neighbor = neighbor.union(ImmediateNeighbors(p))
        imneighbor = neighbor
    return neighbor