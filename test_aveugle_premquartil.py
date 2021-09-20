from premquartil import premquartil

def test_aveugle_premquartilquartil():
    liste=[['A'],['C','G'],['A','C','G'],['A','C','G','T'],['A','C','G','T','A'],['A','C','G','A','C','G'],['A','C','G','T','A','C','G'],['A','C','G','T','A','A','C','G']]
    assert premquartil(liste)==2