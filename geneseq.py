
complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}


def reverse_complement(seq):
    """
    Returns the reversed complement of a sequence

    Args:
        seq (str): the sequence

    Returns: the reversed complement

    """
    seq = seq.upper()

    rseq = []
    for nt in seq:
        rseq.append(complements[nt])
    return ''.join(rseq)[::-1]

