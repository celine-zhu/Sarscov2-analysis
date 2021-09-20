from var_leng import var_leng
from timeit import timeit
from date import date

def test_var_leng():
    L1 = []
    L2 = ['ATC','ATTC','ACGTTAT']
    L3 = ['ATCCC','TAGCTTTAGGGG','ATCCGTA','GATCAAGA']

    assert round(var_leng(L1),2) == 0
    assert round(var_leng(L2),2) == 2.89
    assert round(var_leng(L3),2) == 6.5

def test_time_var_leng():
    L=date(2020,1)
    time=timeit(lambda:var_leng(L),number=1)
    x=len(L)*30000/10**9
    assert time<=x

