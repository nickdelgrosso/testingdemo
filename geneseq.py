

complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}

def reverse_complement(seq):
    seq = seq.upper()
    rseq = []
    for nt in seq:
        rseq.append(complements[nt])
    return ''.join(rseq)[::-1]


def test_complment():
    assert reverse_complement('GCT') == 'AGC'

def test_complement2():
    assert reverse_complement('GGG') != 'AGC'

def test_r3():
    assert reverse_complement('TCCGA') == 'TCGGA'

def test_lower():
    assert reverse_complement('gct') == 'AGC'