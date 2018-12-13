from geneseq import reverse_complement

def test_complment():
    assert reverse_complement('GCT') == 'AGC'


def test_complement2():
    assert reverse_complement('GGG') != 'AGC'


def test_r3():
    assert reverse_complement('TCCGA') == 'TCGGA'


def test_lower():
    assert reverse_complement('gct') == 'AGC'