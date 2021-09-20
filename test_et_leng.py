from et_leng import et_leng
from var_leng import var_leng
from timeit import timeit
from date import date


def test_et_leng():
    L1 = []
    L2 = ['ATC','ATTC','ACGTTAT']
    L3 = ['ATCCC','TAGCTTTAGGGG','ATCCGTA','GATCAAGA']

    assert round(et_leng(L1),2) == 0
    assert round(et_leng(L2),2) == 1.7
    assert round(et_leng(L3),2) == 2.55

def test_time_et_leng():
    L=date(2020,1)
    time=timeit(lambda:et_leng(L),number=1)
    x=len(L)*30000/10**9
    assert time<=x

