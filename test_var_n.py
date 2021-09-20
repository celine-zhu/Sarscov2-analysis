

   
from var_n import var_n 
from fas2ch import fas2ch
from timeit import timeit
                    
def test_var_n():
    liste=[['A','G'],['A','G','C','A'],['A','A','G','C','T','A'],['G','A','T','C','A','A','G','A']]
    n='A'
    assert var_n(liste,n)==1.25
    
def test_time_var_n():
    L=fas2ch('Sequences_2020_01.fasta')
    time=timeit(lambda:var_n(L,'A'),number=1)
    assert time<=9.9*(10^(-4))
    
