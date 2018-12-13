

def reverse_complement(seq):
    seq = seq.upper()
    rseq = []
    for nt in seq:
        if nt == 'G':
            rseq.append('C')
        elif nt == 'C':
            rseq.append('G')
        elif nt == 'T':
            rseq.append('A')
        elif nt == 'A':
            rseq.append('T')
    return ''.join(rseq)[::-1]


def test_complment():
    assert reverse_complement('GCT') == 'AGC'

def test_complement2():
    assert reverse_complement('GGG') != 'AGC'

def test_r3():
    assert reverse_complement('TCCGA') == 'TCGGA'

def test_lower():
    assert reverse_complement('gct') == 'AGC'