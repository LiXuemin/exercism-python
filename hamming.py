def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(".+")
    a = list(strand_a)
    b = list(strand_b)
    hamming = 0
    for i in range(len(strand_a)):
        if a[i] != b[i]:
            hamming += 1
    return hamming
