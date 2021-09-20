

from fas2ch import fas2ch

def test_aveugle_fas2ch1():
    L=fas2ch('Sequences_2020_01.fasta')
    assert type(L)==list and type(L[0]) and type(L[0][0])



def test_aveugle_fas2ch2():
    L=fas2ch('Sequences_2020_01.fasta')
    assert L[0][:6]==['A','T','T','A','A','A']
    

    
