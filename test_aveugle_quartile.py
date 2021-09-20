from premquartil import quartile

def test_aveugle_quartile():
    liste=[['A'],['C','G'],['A','C','G'],['A','C','G','T'],['A','C','G','T','A'],['A','C','G','A','C','G'],['A','C','G','T','A','C','G'],['A','C','G','T','A','A','C','G']]
    assert quartile(liste)==2