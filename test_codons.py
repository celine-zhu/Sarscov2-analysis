from timeit import timeit
from date import date
from codons import codons


#On teste pour une liste créer à la main
def test_codons1():
    seq=['A','G','T','A','C','T','G','T','C','A','G','A']
    assert codons(seq)==['S', 'T', 'V', 'R']

#On teste pour une seq qui a bien une longueur multiple de 3 (len(seq[4])%3==0)
def test_codons2():
    seq=date(2020,1)
    assert codons(seq[4])[:15]==['Q', 'P', 'T', 'F', 'D', 'L', 'L', 'Stop ambre', 'I', 'C', 'S', 'L', 'N', 'E', 'L']

#On teste pour une seq qui n'a pas une longueur multiple de 3 (len(seq[0])%3)
def test_codons_3():
    seq=date(2020,1)
    assert codons(seq[0])==[]

def test_time_codons():
    L=['A','G','T','A','C','T','G','T','C','A','G']
    time=timeit(lambda:codons(L),number=1)
    x=len(L)*30000/10**9
    assert time<=x




