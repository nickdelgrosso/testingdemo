
complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}


def reverse_complement(seq):
    seq = seq.upper()
    rseq = []
    for nt in seq:
        rseq.append(complements[nt])
    return ''.join(rseq)[::-1]

