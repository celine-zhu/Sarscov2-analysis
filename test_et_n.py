
from et_n import et_n                            
from fas2ch import fas2ch
from math import * 
from timeit import timeit
                            
def test_et_n():
    liste=[['A','G'],['A','G','C','A'],['A','A','G','C','T','A'],['G','A','T','C','A','A','G','A']]
    n='A'
    assert et_n(liste,n)==sqrt(1.25)
    
def test_time_et_n():
    L=fas2ch('Sequences_2020_01.fasta')
    time=timeit(lambda:et_n(L,'A'),number=1)
    assert time<=9.9*(10^(-4))