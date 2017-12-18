dnaStr = "GCTA"
dnaDict = {"G" : "C", "C" : "G", "T" : "A", "A" : "U"}
def to_rna(dna_strand):
    l = []
    x = 0
    for i in dna_strand:
        if i not in dnaStr:
            raise ValueError(".+")
        l.insert(x, dnaDict[i])
        x += 1
    return ''.join(l)
