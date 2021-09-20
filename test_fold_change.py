from fold_change import fold_change
from timeit import timeit
from date import date
from var_leng import var_leng
from et_leng import et_leng
from var_n import var_n

def test_fold_change():
    L1 = []
    L2 = ['ATC','ATTC','ACGTTAT']
    L3 = ['ATCCC','TAGCTTTAGGGG','ATCCGTA','GATCAAGA']

    assert round(fold_change(var_leng,L2,L1),2) == 0
    assert round(fold_change(et_leng,L2,L3),2) == 0.67
    assert round(fold_change(var_n,L2,L3,'A'),2) == 0.19

def test_time_fold_change():
    L1=date(2020,1)
    L2=date(2020,2)
    time=timeit(lambda:fold_change(L1,L2,var_leng),number=1)
    x=len(L)*30000/10**9
    assert time<=x